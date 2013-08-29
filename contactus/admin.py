from django.contrib import admin
from contactus.models import ContactUs

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    list_editable = ('message',)

admin.site.register(ContactUs, ContactUsAdmin)
