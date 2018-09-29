from django import forms
from .models import *

class feed_back_form(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(), required=True, max_length=100)
    msg = forms.CharField(widget=forms.TextInput(), required=True, max_length=1000)

    class Meta():
        model = feed_back
        fields = ['email','msg']