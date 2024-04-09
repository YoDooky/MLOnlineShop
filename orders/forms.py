from django import forms
from django.db import models
import re


class Delivery(models.IntegerChoices):
    DELIVERY = 0, 'Delivery'
    PICKUP = 1, 'Self pickup'


class Payment(models.IntegerChoices):
    CARD = 0, 'By card'
    CASH = 1, 'By cash'


class OrderForm(forms.Form):
    first_name = forms.CharField(label='First name: ', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last name: ', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    phone_number = forms.CharField(label='Phone number: ', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Format: XXX-XXX-XX-XX'
        }))
    requires_delivery = forms.CharField(label='Delivery method: ', required=False, widget=forms.RadioSelect(
        choices=Delivery.choices,
        attrs={'class': 'form-check-input'}
    ), initial=0)
    delivery_address = forms.CharField(required=False, label='Delivery address: ', widget=forms.Textarea(
        attrs={'class': 'form-control',
               'rows': 2}))
    payment_on_get = forms.CharField(label='Payment method: ', required=False, widget=forms.RadioSelect(
        choices=Payment.choices,
        attrs={'class': 'form-check-input'}
    ), initial=0)

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if not phone_number.isdigit():
            raise forms.ValidationError('Phone number must contain only digits')
        pattern = re.compile(r'^\d{10}$')
        if not pattern.match(phone_number):
            raise forms.ValidationError('Wrong number format')
        return phone_number
