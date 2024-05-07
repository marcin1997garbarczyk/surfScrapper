from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SubscriberFormSerializer
from .models import Subscriber, Beach
from .surfScrapperEngine.controllers import webscrapperController

from .surfScrapperEngine.services.accountService import AccountService
from .surfScrapperEngine.services.emailService import EmailService
from .tasks import sendEmailsToSubscribers

accountService = AccountService()
emailService = EmailService()

class BestSpotsInAlgarveApiView(APIView):
    def get(self, request, format=None):
        beach_data_from_db = webscrapperController.getSortedBeachesInJSON(Beach)
        return Response({'beach_data_from_db': beach_data_from_db}, status=status.HTTP_200_OK, content_type='application/json')

class AvailableBeachesApiView(APIView):
    def get(self, request, format=None):
        beach_names = webscrapperController.getNameOfBeachesInAlgarve()
        return Response({'beach_names': beach_names}, status=status.HTTP_200_OK, content_type='application/json')

class ActivationOfEmail(APIView):
    def get(self, request, uidb64, token):
        isSuccess = accountService.activateUser(subscriberModel=Subscriber, uidb64=uidb64, token=token)
        if(isSuccess):
            return render(request, 'activationPage.html', {'message':'Your subscription is active now!'})
        else:
            return render(request, 'activationPage.html', {'message':'Something went wrong! Try register again!'})

class SubmitSubscriberFormView(APIView):
    def post(self, request, format=None):
        serializer = SubscriberFormSerializer(data=request.data)
        isSuccess = accountService.upsertSubscription(request, Subscriber, serializer)
        if isSuccess:
            return Response({'message': 'Form submitted successfully!'}, status=status.HTTP_201_CREATED, content_type='application/json')
        else:
            return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class SendEmailToSubscribersView(APIView):
    def get(self):
        sendEmailsToSubscribers()