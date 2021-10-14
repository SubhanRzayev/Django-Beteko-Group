from django import forms
from django.db.models import fields
from rest_framework.utils import model_meta
from core.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'subject',
            'message',
        )

        widgets = {

            'name':forms.TextInput(attrs={
                        'class':'control-group',
                        'placeholder': 'Your Name'
                    }),

            'email':forms.EmailInput(attrs={
                'class':'control-group',
                'placeholder': 'Your email'
            }),

            'subject':forms.TextInput(attrs={
                'class':'control-group',
                'placeholder': 'Write subject'
            }),

            'message':forms.Textarea(attrs={
                'class': 'control-group',
                'placeholder': 'Your message'
            }),
        }


from django.forms import widgets
from .models import Subscriber

class SubScriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = '__all__'

        widgets = {
            'email':forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder':'Email here',
            }),
        }    
