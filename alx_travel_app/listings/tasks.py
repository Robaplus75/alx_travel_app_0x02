from celery import shared_task
from time import sleep

@shared_task
def send_email(message):
    sleep(15)
    return "Email Message Send"
