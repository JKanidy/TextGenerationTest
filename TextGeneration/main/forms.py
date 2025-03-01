from django import forms
from django.forms import ModelForm
from .models import UserInput
class UserInputForm(ModelForm):
    text = forms.TextInput()
    class Meta:
        model = UserInput
        fields = ['text']