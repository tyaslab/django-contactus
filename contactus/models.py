from django.db import models

class AbstractContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    class Meta:
        abstract = True

class ContactUs(AbstractContactUs):
    phone = models.CharField(max_length=30)
    class Meta:
        pass
    
    def __unicode__(self):
        return '%s %s' % (self.name, self.email)
