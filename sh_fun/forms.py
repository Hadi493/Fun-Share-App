from django import forms
from .models import Fun

class FunForm(forms.ModelForm):
    class Meta:
        model = Fun
        fields = ['text', 'photo']