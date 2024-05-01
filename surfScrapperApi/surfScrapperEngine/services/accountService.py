from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from surfScrapperApi.surfScrapperEngine.controllers.webscrapperController import getRatingForSelectedBeaches
from surfScrapperApi.surfScrapperEngine.services.emailService import EmailService


class AccountService:

    def __init__(self):
        self.tokenGenerator = TokenGenerator()
    def getTokenForUser(self, user):
        return self.tokenGenerator.make_token(user)
    def checkTokenForUser(self, user, token):
        return self.tokenGenerator.check_token(user, token)

    def upsertSubscription(self, request, subscriberModel, serializer):
        if serializer.is_valid():
            try:
                obj = subscriberModel.objects.get(userEmail=serializer.data.get('userEmail'))
                obj.trackedBeaches = serializer.data.get('trackedBeaches')
                obj.save()
            except(TypeError, ValueError, OverflowError, subscriberModel.DoesNotExist):
                obj = subscriberModel()
                obj.userEmail = serializer.data.get('userEmail')
                obj.trackedBeaches = serializer.data.get('trackedBeaches')
                obj.save()

            print(f'Save {obj.pk}')
            if(obj.isActive):
                EmailService().sendInformativeEmail(obj)
            else:
                EmailService().sendActivationEmail(request, obj, self.getTokenForUser(obj))

            return True
        else:
            return False

    def activateUser(self, subscriberModel, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = subscriberModel.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, subscriberModel.DoesNotExist):
            user = None
        if user is not None and AccountService().checkTokenForUser(user, token):
            user.isActive = True
            user.save()
            return True
        else:
            return False

    def sendRatingsToActiveUsers(self, subscriberModel):
        activeSubscribers = subscriberModel.objects.filter(isActive = True)
        for subscriberObj in activeSubscribers:
            nameOfTrackedBeaches = subscriberObj.trackedBeaches.split(',')
            ratingForBeaches = getRatingForSelectedBeaches(nameOfTrackedBeaches)[:3]
            ratingForBeachesText = str(ratingForBeaches)[2:len(str(ratingForBeaches))-2].replace("', '", '').encode().decode('unicode-escape')
            print(f'best: {ratingForBeachesText}')
            EmailService().sendRatingEmail(subscriberObj, ratingForBeachesText)

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                text_type(user.pk) + text_type(timestamp) +
                text_type(user.isActive)
        )

