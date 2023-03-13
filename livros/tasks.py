from __future__ import absolute_import, unicode_literals

from celery import shared_task

from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_notification(user, book, status):
    try:
        book_name = book.title
        user_email = user.email
        subject = f'Você está seguindo o livro {book_name}'

        if status == "following":
            message = f'Você está seguindo o livro: {book_name} e receberá notificações sobre o atual estado do livro a cada empréstimo.'
        elif status == "available":
            message = f'Uma cópia do livro {book_name} foi emprestada mas o mesmo ainda encontra-se disponível para empréstimo.'
        elif status == "unfollowing":
            subject = f'Você parou de seguir o livro {book_name}.'
            message = f'Você parou de segir o livro {book_name} e por isso não irá receber mais notificações sobre seu estado!'
        else:
            message = f'O livro {book_name} não se encontra mais disponível para empréstimo.'

        email_from = settings.EMAIL_HOST_USER
        recipient = [user_email]

        send_mail(subject, message, email_from, recipient)

    except Exception as e:
        print(e)