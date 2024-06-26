import random

from celery import shared_task
from celery.beat import logger

from surfScrapperApi.models import Subscriber, Beach
from surfScrapperApi.surfScrapperEngine.controllers import webscrapperController
from surfScrapperApi.surfScrapperEngine.services.accountService import AccountService
from surfScrapperApi.surfScrapperEngine.services.emailService import EmailService

accountService = AccountService()

@shared_task
def sendEmailsToSubscribers():
    logger.info("Executing Mail Task")
    accountService.sendRatingsToActiveUsers(Subscriber)

@shared_task
def scrapeForecastAndUploadDb():
    logger.info("Executing Upload Db Task")
    webscrapperController.scrapeAndUploadAllBeachesToDb(Beach)