import random

from celery import shared_task
from celery.beat import logger

from surfScrapperApi.models import Subscriber
from surfScrapperApi.surfScrapperEngine.services.emailService import EmailService


@shared_task
def sendEmailsToSubscribers():
    print('Schedule example job')
    logger.info("Executing Task")
    obj = Subscriber.objects.get(userEmail='marcin1997garbarczyk@gmail.com')
    EmailService().sendInformativeEmail(obj)