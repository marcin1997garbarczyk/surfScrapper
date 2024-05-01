import random

from celery import shared_task
from celery.beat import logger

from surfScrapperApi.models import Subscriber
from surfScrapperApi.surfScrapperEngine.services.accountService import AccountService
from surfScrapperApi.surfScrapperEngine.services.emailService import EmailService

accountService = AccountService()

@shared_task
def sendEmailsToSubscribers():
    print('Schedule example job')
    logger.info("Executing Task")
    accountService.sendRatingsToActiveUsers(Subscriber)