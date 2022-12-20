from typing import Text
from django import forms

class FormContact(forms.Form):
    name = forms.CharField(label="Name", required=True)
    email = forms.EmailField(label="email", required=True)
    contact = forms.CharField(label="contact", widget=forms.Textarea)
    