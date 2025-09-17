from django import forms
from .models import Destination,Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class DestinationForm(forms.ModelForm):
    class Meta:
        model=Destination
        fields = ['name','category','country', 'image', 'description', 'price']




