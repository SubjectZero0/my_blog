from django.shortcuts import render
from django.views.generic import CreateView,TemplateView
from .forms import ContactModelForm

from .models import Subscriber, Contact
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

class SubscriberForm(CreateView):
    model = Subscriber
    fields = '__all__'
    success_url = reverse_lazy('my_blog:home')


    # this method allows for use of {{subscriber_form}} instead of {{form}} in html
    def get_context_data(self, **kwargs):
            context = super(SubscriberForm, self).get_context_data(**kwargs)
            context["subscriber_form"]=context["form"]
            return context
    

########################################################################
########################################################################
########################################################################

class ContactForm(CreateView):
    model = Contact
    form_class = ContactModelForm
    template_name = 'emails/Contact_form.html'
    success_url = reverse_lazy('emails:contact_thank_you')


# this method allows for use of {{contact_form}} instead of {{form}} in html
    def get_context_data(self, **kwargs):
        context = super(ContactForm, self).get_context_data(**kwargs)
        context['contact_form'] = context['form']
        return context

    # this method sends an email to me with the content of the feedback

    def form_valid(self, form):
        instance_f_name = form.cleaned_data.get('f_name')
        instance_l_name = form.cleaned_data.get('l_name')
        instance_email = form.cleaned_data.get('email')
        instance_feedback = form.cleaned_data.get('feedback')

        sbj = f'{str.capitalize(instance_f_name)} {str.capitalize(instance_l_name)} with email: {instance_email}, left some feedback.'
        msg = instance_feedback
        sender = instance_email
        
        send_mail(
            subject= sbj,
            message = msg,
            from_email = sender,
            recipient_list= [settings.EMAIL_HOST_USER],
            fail_silently= False

        )
        return super(ContactForm, self).form_valid(form)

    
class ContactThankYou(TemplateView):
    template_name = 'emails/contact_thank_you.html'