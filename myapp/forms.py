from django.forms import ModelForm
from django import forms

from myapp.models import case

from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    password2 = forms.CharField(
        label='confirm Password(again)', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        label = {'email': 'Email'}


class caseForm(ModelForm):
    class Meta:
        model = case
        exclude = ['gravity']
        widgets = {
            'last_hearing_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'chart_sheet_filling_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'section': forms.TextInput(attrs={'class': 'input-field '}),
            'case_No': forms.TextInput(attrs={'class': 'input-field '}),
            'case_type': forms.TextInput(attrs={'class': 'input-field '}),
            'case_statement': forms.TextInput(attrs={'class': 'input-field '}),
        }
