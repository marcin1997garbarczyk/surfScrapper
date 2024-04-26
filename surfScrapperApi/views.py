from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import render, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from six import text_type

from .models import Subscriber
from .serializers import SubscriberFormSerializer
from .surfScrapperEngine.controllers import webscrapperController
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_str
class AvailableBeachesApiView(APIView):
    def get(self, request, format=None):
        beach_names = webscrapperController.getNameOfBeachesForApi()
        return Response({'beach_names': beach_names}, status=status.HTTP_200_OK, content_type='application/json')

class ActivationOfEmail(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = Subscriber.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, Subscriber.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.isActive = True
            user.save()
            return render(request, 'activationPage.html', {'message':'Your subscription is active now!'})
        else:
            return render(request, 'activationPage.html', {'message':'Something went wrong! Try register again!'})

class SubmitSubscriberFormView(APIView):
    def post(self, request, format=None):
        serializer = SubscriberFormSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            print(f'Save {obj.pk}')
            self.sendActivationEmail(request, obj)
            return Response({'message': 'Form submitted successfully!'}, status=status.HTTP_201_CREATED, content_type='application/json')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def sendActivationEmail(self, request, user):
        mail_subject = 'Activate your subscription.'
        message = render_to_string(
            'emailTemplate.html',
            {
                'user': user,
                'domain': get_current_site(request).domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            }
        )
        to_email = user.userEmail
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                text_type(user.pk) + text_type(timestamp) +
                text_type(user.isActive)
        )

account_activation_token = TokenGenerator()