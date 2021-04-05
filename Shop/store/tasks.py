
import requests  # noqa
from celery import shared_task

from django.core.mail import send_mail

from .models import Book, Author, Category

@shared_task
def send_mail_task(subject, message, email):
    send_mail(subject, message, email, ['admin@example.com'])


@shared_task
def data_synchronization():
    # url_adress = 'http://127.0.0.1:8002/api/book/'
    # # url_author = 'http://127.0.0.1:8002/api/author/'
    # url_category = 'http://127.0.0.1:8002/api/category/'
    #
    # response = requests.get(url_adress).json()
    # # response_author = requests.get(url_author).json()
    # response_category = requests.get(url_category).json()
    url_author = 'http://127.0.0.1:8002/api/author/'
    response_author = requests.get(url_author).json()
    while 1:
        for count, author in enumerate(response_author['results']):
            data1, created = Author.objects.get_or_create(
                id=author['id'],
                defaults={
                    'name': author['name']
                }
            )
            if not created:
                data1.name = author['name']
                data1.save()

        if response_author['next']:
            response_author = requests.get(response_author['next']).json()
        else:
            break

    url_category = 'http://127.0.0.1:8002/api/category/'
    response_category = requests.get(url_category).json()
    while 1:
        for count, category in enumerate(response_category['results']):
            data2, created = Category.objects.get_or_create(
                id=category['id'],
                defaults={
                    'id': category['id'],
                    'name': category['name']
                }
            )
            if not created:
                data2.name = category['name']
                data2.save()

        if response_category['next']:
            response_category = requests.get(response_category['next']).json()
        else:
            break

    url_adress = 'http://127.0.0.1:8002/api/book/'
    response = requests.get(url_adress).json()
    while 1:
        for counter, book in enumerate(response['results']):
            data, created = Book.objects.get_or_create(
                    id=book['id'],
                    defaults={
                        'title': book['title'],
                        'price': book['price'],
                        'image': book['image'],
                        'publication_year': book['publication_year'],
                        'status': book['status'],
                        'rating': book['rating'],
                        'description': book['description'],
                        'category': Category.objects.get(id=book['category'])
                    }

            )
            if not created:
                data.title = book['title']
                data.price = book['price']
                data.image = book['publication_year']
                data.status = book['status']
                data.rating = book['rating']
                data.description = book['description']
                data.image = book['image']
                data.category = Category.objects.get(id=book['category'])
                data.save()

            for pk in book['author']:
                au = Author.objects.get(id=pk)
                data.author.add(au)
                data.save()

        if response['next']:
            response = requests.get(response['next']).json()
        else:
            break

    print('Sync is done')