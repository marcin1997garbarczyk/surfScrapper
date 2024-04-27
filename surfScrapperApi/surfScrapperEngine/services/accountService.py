from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from surfScrapperApi.surfScrapperEngine.services.emailService import EmailService


class AccountService:

    def __init__(self):
        self.tokenGenerator = TokenGenerator()
    def getTokenForUser(self, user):
        return self.tokenGenerator.make_token(user)
    def checkTokenForUser(self, user, token):
        return self.tokenGenerator.check_token(user, token)

    def createNewUser(self, request, serializer):
        if serializer.is_valid():
            obj = serializer.save()
            print(f'Save {obj.pk}')
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

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                text_type(user.pk) + text_type(timestamp) +
                text_type(user.isActive)
        )

