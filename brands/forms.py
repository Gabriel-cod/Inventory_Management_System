from .models import Brand
from django import forms


class BrandForm(forms.ModelForm):

    class Meta:
        model = Brand
        fields = ('name', 'description',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'id_description'}),
        }
