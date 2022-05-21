from django import forms


class PreOrderForm(forms.Form):
    color = forms.CharField()
    option = forms.CharField()
    shoe_size = forms.CharField()
    clothing_size = forms.CharField()
