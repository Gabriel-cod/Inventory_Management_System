from django import forms
from .models import Supplier


class SupplierForm(forms.ModelForm):

    class Meta:
        model = Supplier
        fields = ('name', 'description')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'id_description'}),
        }
