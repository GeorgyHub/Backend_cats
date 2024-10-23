from django import forms
from django.contrib.auth.models import User
from .models import Cats

# form for create cats
class CatsForm(forms.ModelForm):
    class Meta:
        model  = Cats
        fields = ['name', 'age', 'breed', 'hairiness']
        widgets = {}