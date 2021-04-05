import uuid

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
# Create your models here


User = get_user_model()


class Author(models.Model):

    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Category(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):

    class LoanStatus(models.IntegerChoices):
        AVAILABLE = 1, _('available')
        NOT_AVAILABLE = 2, _('not available')

    description = models.TextField()
    title = models.CharField(max_length=255)
    author = models.ManyToManyField(Author)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/images', blank=True)
    publication_year = models.PositiveSmallIntegerField()
    status = models.PositiveSmallIntegerField(
        choices=LoanStatus.choices, default=LoanStatus.AVAILABLE, blank=True
    )
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.title


class Order(models.Model):

    class OrderStatus(models.IntegerChoices):
        WAITING = 1, _('Waiting')
        IN_PROGRESS = 2, _('In progress')
        DONE = 3, _('Done')

    phone = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    status = models.PositiveSmallIntegerField(
        choices=OrderStatus.choices, default=OrderStatus.WAITING, blank=True
    )


class OrderItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=9, decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class BookInstance(models.Model):

    class InstanceStatus(models.IntegerChoices):
        RESERVED = 1, _('Reserved'),
        IN_STOCK = 2, _('In stock'),
        SOLD = 3, _('Sold')

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    item_of_order = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    book_status = models.PositiveSmallIntegerField(
        choices=InstanceStatus.choices, default=InstanceStatus.IN_STOCK
    )

