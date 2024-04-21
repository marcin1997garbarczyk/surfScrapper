# api/urls.py
from django.urls import path
from .views import SubmitSubscriberFormView

urlpatterns = [
    path('submit_subscriber_form', SubmitSubscriberFormView.as_view(), name='submit_subscriber_form'),
]