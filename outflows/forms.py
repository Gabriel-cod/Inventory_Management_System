from django import forms
from django.core.exceptions import ValidationError
from .models import Outflow


class OutflowForm(forms.ModelForm):

    class Meta:
        model = Outflow
        fields = ('product', 'quantity', 'description')
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        product = self.cleaned_data['product']
        if quantity > product.quantity:
            raise ValidationError(f"We don't have {quantity} {product} in inventory.\
                We have {product.quantity} units of this product.")
        if quantity <= 0:
            raise ValidationError('The quantity must be greater than 0.')
        return quantity
