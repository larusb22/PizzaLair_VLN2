from django import forms
from account.models import AccountInformation, Profile
from django.forms import ModelForm, widgets


from django.forms import ModelForm, widgets


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user']
        widgets = {
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'profile_image': widgets.TextInput(attrs={'class': 'form-control'})
        }

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
                ('ICE', 'Iceland'),
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
                ('ICE', 'Iceland'),
            ])
        }


class CreditCardForm(forms.Form):

    credit_card_number = forms.CharField(max_length=16)
    expiry_date = forms.CharField()
    cvc_number = forms.CharField(max_length=3)


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user']
        widgets = {
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'profile_image': widgets.TextInput(attrs={'class': 'form-control'})
        }