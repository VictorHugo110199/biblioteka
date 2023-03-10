from __future__ import absolute_import, unicode_literals

from celery import shared_task

from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_notification(user, book, available=True):
    try:
        book_name = book.title
        user_email = user.email

        if available:
            message = f'Uma cópia do livro {book_name} foi emprestada mas o mesmo ainda encontra-se disponível para empréstimo.'
        else:
            message = f'O livro {book_name} não se encontra disponível para empréstimo.'

        subject = f'Você está seguindo o livro {book_name}'
        email_from = settings.EMAIL_HOST_USER
        recipient = [user_email]

        send_mail(subject, message, email_from, recipient)

    except Exception as e:
        print(e)