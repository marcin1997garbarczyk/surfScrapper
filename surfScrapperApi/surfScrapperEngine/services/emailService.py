
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

import config


class EmailService:

    def sendInformativeEmail(self, user):
        mail_subject = 'Change your subscription.'
        message = render_to_string(
            'changeEmailTemplate.html',
            {
                'user': user,
            }
        )
        to_email = user.userEmail
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()

    def sendRatingEmail(self, user, ratingForBeaches):
        message = render_to_string(
            template_name='ratingEmailTemplate.html',
            context= {
                'user': user,
                'ratingForBeaches': ratingForBeaches
            }
        )
        plain_message = strip_tags(message)

        yo_send_it = send_mail(
            subject="Rating in algarve for you!",
            message=plain_message,
            from_email='surfscrapper@gmail.com',
            recipient_list=[user.userEmail],
            html_message = message
        )


    def sendActivationEmail(self, request, user, userToken):
        mail_subject = 'Activate your subscription.'
        message = render_to_string(
            'activateEmailTemplate.html',
            {
                'user': user,
                'domain': get_current_site(request).domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': userToken,
            }
        )
        to_email = user.userEmail
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()

