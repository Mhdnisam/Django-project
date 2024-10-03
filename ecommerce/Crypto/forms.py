from django import forms
from django.contrib.auth.models import User
from . import models
from.models import User, Customer


class CustomerUserForm(forms.ModelForm):
    class meta:
        model = User
        fields =['first_name','lastname','username','password']
        widgets = {
            'password': forms.PasswordInput()
        }
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['address', 'mobile','profile_pic']