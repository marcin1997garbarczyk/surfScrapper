
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


class EmailService:
    def sendActivationEmail(self, request, user, userToken):
        mail_subject = 'Activate your subscription.'
        message = render_to_string(
            'emailTemplate.html',
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

