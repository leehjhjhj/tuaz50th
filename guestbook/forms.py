from django import forms
from .models import Balloon

class BalloonForm(forms.ModelForm):
    class Meta:
        model = Balloon
        fields = ['body']
    
    def clean_body(self):
        body = self.cleaned_data.get('body')
        if len(body) > 50:
            raise forms.ValidationError("50자 이하여야 합니다.")
        return body