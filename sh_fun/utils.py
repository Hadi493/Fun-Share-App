from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string
from django.urls import reverse

def send_verification_email(user, request):
    """Send verification email to user"""
    token = get_random_string(64)
    user.userprofile.email_verification_token = token
    user.userprofile.save()
    
    verification_url = request.build_absolute_uri(
        reverse('verify_email', kwargs={'token': token})
    )
    
    subject = 'Verify your Fun App email address'
    message = render_to_string('email/verification_email.html', {
        'user': user,
        'verification_url': verification_url,
    })
    
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
        html_message=message
    )