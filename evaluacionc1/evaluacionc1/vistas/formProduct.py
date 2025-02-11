from django import forms
from ..models import Product, Category

class FormProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'amount', 'id_category']
        labels = {
            'name': 'Nombre del producto',
            'description': 'Descripción',
            'price': 'Precio',
            'amount': 'Cantidad',
            'id_category': 'Categoría',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'id_category': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Product.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError('Ya existe un producto con este nombre.')
        return name

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 1:
            raise forms.ValidationError('El precio debe ser mayor a 0.')
        return price

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount < 0:
            raise forms.ValidationError('La cantidad no puede ser negativa.')
        return amount

    def save(self, commit=True):
        product = super().save(commit=False)
        if commit:
            product.save()
        return product
