from django import forms
from ..models import OrderProduct, Orders, Product

class FormOrderProduct(forms.ModelForm):
    class Meta:
        model = OrderProduct
        fields = ['id_order', 'id_product']
        labels = {
            'id_order': 'Orden',
            'id_product': 'Producto',
        }
        widgets = {
            'id_order': forms.Select(attrs={'class': 'form-control'}),
            'id_product': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        id_order = cleaned_data.get('id_order')
        id_product = cleaned_data.get('id_product')

        if OrderProduct.objects.filter(id_order=id_order, id_product=id_product).exists():
            raise forms.ValidationError('Este producto ya está en la orden.')

        return cleaned_data
