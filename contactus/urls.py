from django.conf.urls import patterns, include, url

from .views import ContactUsView

urlpatterns = patterns('',
    url(r'^$', ContactUsView.as_view(), name='contact'),
)
