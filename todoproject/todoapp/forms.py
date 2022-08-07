from .models import task
from  django import forms

class taskform(forms.ModelForm):
    class Meta:
        model=task
        fields=['name','priority','date']
