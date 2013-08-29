from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from contactus.forms import ContactUsForm
from django.conf import settings

from .models import ContactUs
from django.views.generic.edit import CreateView

class ContactUsView(CreateView):
    model = ContactUs
    form_class = ContactUsForm
    
    def send_email(self):
        if hasattr(settings, 'CONTACTUS_DEFAULT_TO'):
            email_to = settings.CONTACTUS_DEFAULT_TO
            if not hasattr(settings, 'CONTACTUS_DEFAULT_SUBJECT'):
                email_subject = 'New message from %s' % (self.object.email,)
            else:
                email_subject = settings.CONTACTUS_DEFAULT_SUBJECT
            
            send_mail(email_subject, self.object.message, self.object.email, [email_to])
        else:
            pass
    
    def get_success_url(self):
        self.send_email()
        return reverse('contact')
