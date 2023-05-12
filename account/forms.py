from django import forms
from account.models import AccountInformation


class UnregisteredUserForm(forms.ModelForm):
    class Meta:
        model = AccountInformation
        fields = ['first_name', 'last_name', 'country', 'city', 'house_address', 'house_number', 'postal_code']
        widgets = {
            'country': forms.Select(choices=[
                ('', '---'),
                ('USA', 'United States of America'),
                ('CAN', 'Canada'),
                ('GBR', 'United Kingdom'),
                ('FRA', 'France'),
                ('DEU', 'Germany'),
            ])
        }


class RegisteredUserForm(forms.ModelForm):
    class Meta:
        model = AccountInformation
        fields = ['country', 'city', 'house_address', 'house_number', 'postal_code']
        widgets = {
            'country': forms.Select(choices=[
                ('', '---'),
                ('USA', 'United States of America'),
                ('CAN', 'Canada'),
                ('GBR', 'United Kingdom'),
                ('FRA', 'France'),
                ('DEU', 'Germany'),
            ])
        }


class CreditCardForm(forms.Form):

    credit_card_number = forms.CharField(max_length=16)
    expiry_date = forms.CharField()
    cvc_number = forms.CharField(max_length=3)