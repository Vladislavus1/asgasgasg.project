from django import forms
from .models import Message


class Form(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']
        labels = {
            'text': 'Text'
        }
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }