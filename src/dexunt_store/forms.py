from django import forms
from phonenumber_field.formfields import PhoneNumberField


class PreOrderForm(forms.Form):
    color = forms.CharField()
    option = forms.CharField()
    shoe_size = forms.CharField()
    clothing_size = forms.CharField()


class OrderForm(forms.Form):
    quantity = forms.IntegerField()
    client_name = forms.CharField()
    client_phone = PhoneNumberField()
    delivery = forms.CharField()
    destination = forms.CharField()
    coupon = forms.CharField()

