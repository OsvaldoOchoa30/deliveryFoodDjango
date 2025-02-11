from django import forms
from ..models import Orders, Customer, Delivery

class FormOrders(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['id_customer', 'id_delivery']
        labels = {
            'id_customer': 'Cliente',
            'id_delivery': 'Repartidor',
        }
        widgets = {
            'id_customer': forms.Select(attrs={'class': 'form-control'}),
            'id_delivery': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_customer'].widget.attrs['autofocus'] = True

    def clean_id_customer(self):
        id_customer = self.cleaned_data.get('id_customer')
        if not id_customer:
            raise forms.ValidationError('Debe seleccionar un cliente.')
        return id_customer

    def clean_id_delivery(self):
        id_delivery = self.cleaned_data.get('id_delivery')
        if id_delivery and not id_delivery.status:
            raise forms.ValidationError('El repartidor seleccionado no está disponible.')
        return id_delivery

    def save(self, commit=True):
        order = super().save(commit=False)
        if commit:
            order.save()
        return order
