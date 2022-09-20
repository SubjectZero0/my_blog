from django.urls import path
from .views import ContactForm, ContactThankYou



app_name = 'emails'

urlpatterns = [

     path('contact/', ContactForm.as_view(), name='contact_page'),
     path('contact/thank_you/', ContactThankYou.as_view(), name = 'contact_thank_you')

]