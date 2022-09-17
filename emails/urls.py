from django.urls import path
from .views import ContactForm, SubscriberForm, ContactThankYou
from my_blog.views import HomeTemplateView


app_name = 'emails'

urlpatterns = [

     path('subscribe/', SubscriberForm.as_view(), name = 'subscriber_form'),
     path('contact/', ContactForm.as_view(), name='contact_page'),
     path('contact/thank_you/', ContactThankYou.as_view(), name = 'contact_thank_you')

]