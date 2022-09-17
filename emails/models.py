from django.utils import timezone
from django.db import models

# Create your models here.

# Subscribers. These users will be able to get notification emails for new posts.
class Subscriber(models.Model):
    f_name = models.CharField(max_length=30, verbose_name='First Name')
    l_name = models.CharField(max_length=30, verbose_name='Last Name')
    email = models.EmailField(verbose_name='Email')

    def __str__(self):
        return self.email


#########################################
#########################################
#########################################

class Contact(models.Model):
    f_name = models.CharField(max_length=30, verbose_name='First Name')
    l_name = models.CharField(max_length=30, verbose_name='Last Name')
    email = models.EmailField(verbose_name='Email')
    date = models.DateTimeField(default=timezone.now)
    feedback = models.TextField(verbose_name="Tell us what's on your mind!")

    def __str__(self):
        return self.email