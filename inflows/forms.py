from django import forms
from django.core.exceptions import ValidationError
from .models import Inflow


class InflowForm(forms.ModelForm):

    class Meta:
        model = Inflow
        fields = ('product', 'supplier', 'quantity', 'description')
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity <= 0:
            raise ValidationError('The quantity must be greater than 0.')
        return quantity
