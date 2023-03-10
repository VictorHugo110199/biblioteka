from __future__ import absolute_import, unicode_literals

from celery import shared_task

from django.core.mail import send_mail
from copias.models import Copy
from django.conf import settings


@shared_task
def send_notification(user, book):
    try:
        book_name = book.title
        user_email = user.email

        subject = f'Você está seguindo o livro {book_name}'
        message = f'O livro {book_name} encontra-se disponível para empréstimo.'
        email_from = settings.EMAIL_HOST_USER
        recipient = [user_email]

        send_mail(subject, message, email_from, recipient)

    except Exception as e:
        print(e)