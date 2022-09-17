from ast import Sub
from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Subscriber

class SubscriberForm(ModelForm):
    class Meta:
        model = Subscriber
        fields = '__all__'
        widgets = {

            'f_name' : forms.TextInput(attrs={'class':'form-control',
                                                'id':'floatingInput',
                                                'placeholder':'Name Here'}),

            'l_name' : forms.TextInput(attrs={'class':'form-control',
                                                'id':'floatingInput',
                                                'placeholder':'Last Name Here'}),

            'email' : forms.EmailInput(attrs={'class':'form-control',
                                                'id':'floatingInput',
                                                'placeholder':'Email Here'}),
        }



    






        
