from django import forms
from django.conf import settings
from django.core.mail import BadHeaderError, EmailMessage

class ContactUs (forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(label=" Your Email")
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)








