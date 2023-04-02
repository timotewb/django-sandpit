from django import forms
from . import models

class AddPerson(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = models.Ftree_Hierarchy