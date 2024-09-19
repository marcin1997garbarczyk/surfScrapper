# api/urls.py
from django.urls import include, path
from .views import SubmitSubscriberFormView, AvailableBeachesApiView, ActivationOfEmail, BestSpotsInAlgarveForTomorrowApiView, SendEmailToSubscribersView, BestSpotsInAlgarveForTodayApiView

urlpatterns = [
    path('submit_subscriber_form', SubmitSubscriberFormView.as_view(), name='submit_subscriber_form'),
    path('get_available_beaches', AvailableBeachesApiView.as_view() , name='get_available_beaches'),
    path('get_best_spots_for_tomorrow', BestSpotsInAlgarveForTomorrowApiView.as_view(), name='get_best_spots_for_tomorrow'),
    path('get_best_spots_for_today', BestSpotsInAlgarveForTodayApiView.as_view(), name='get_best_spots_for_today'),
    path('activate/<uidb64>/<token>/', ActivationOfEmail.as_view(), name='activate'),
    path('update', SendEmailToSubscribersView.as_view(), name='update'),
]