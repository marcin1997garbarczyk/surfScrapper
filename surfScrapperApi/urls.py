# api/urls.py
from django.urls import path
from .views import SubmitSubscriberFormView, AvailableBeachesApiView, ActivationOfEmail

urlpatterns = [
    path('submit_subscriber_form', SubmitSubscriberFormView.as_view(), name='submit_subscriber_form'),
    path('get_available_beaches', AvailableBeachesApiView.as_view() , name='get_available_beaches'),
    path('activate/<uidb64>/<token>/', ActivationOfEmail.as_view(), name='activate'),
]