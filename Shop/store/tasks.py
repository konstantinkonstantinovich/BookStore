from celery import shared_task

from django.core.mail import send_mail


@shared_task
def send_mail_task(subject, message, email):
    send_mail(subject, message, email, ['admin@example.com'])
