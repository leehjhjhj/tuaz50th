from django import forms
from .models import Balloon

class BalloonForm(forms.ModelForm):
    class Meta:
        model = Balloon
        fields = ['body']
