from .models import Category
from django import forms


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name', 'description',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_name'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_description'}),
        }
