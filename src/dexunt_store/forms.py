from django import forms
from phonenumber_field.formfields import PhoneNumberField


class PreOrderForm(forms.Form):
    color = forms.CharField()
    option = forms.CharField()
    shoe_size = forms.CharField()
    clothing_size = forms.CharField()


class OrderForm(forms.Form):
    quantity = forms.IntegerField(required=True)
    client_name = forms.CharField(required=True)
    client_phone = PhoneNumberField(required=True)
    delivery = forms.CharField(required=True)
    destination = forms.CharField(required=True)
    coupon = forms.CharField()

