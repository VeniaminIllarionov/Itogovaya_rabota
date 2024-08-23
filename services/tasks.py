from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from celery import shared_task

from services.models import Record


@shared_task
def send_email_task(service_id):
    """
    Send email to user
    """
    subs = Record.objects.filter(service=service_id)
    for sub in subs:
        service = sub.service
        user = sub.user
        send_mail('Обновление', 'Ваша подписка на курсе обновилась'.format(service.name),
                  EMAIL_HOST_USER, [user.email])
        print(f'Письмо отправлено пользователю {user.email}')

