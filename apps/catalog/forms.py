from django import forms

def clean_quantity(self):
    quantity = self.cleaned_data.get('quantity')
    if self.product:
        if quantity > self.product.quantity:
            raise forms.ValidationError("Недостатньо товару на складі")
    return quantity