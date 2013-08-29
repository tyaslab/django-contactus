from django.forms import ModelForm
from contactus.models import ContactUs
from captcha.fields import ReCaptchaField

class ContactUsForm(ModelForm):
    recaptcha = ReCaptchaField(public_key='6LdaQN8SAAAAADMYVOUJRDEaG-wrJMdp892So9WD', private_key='6LdaQN8SAAAAAKQf6vH4okS0yU0JhaKg-SrAr5e5', use_ssl=True)
    class Meta:
        model = ContactUs
