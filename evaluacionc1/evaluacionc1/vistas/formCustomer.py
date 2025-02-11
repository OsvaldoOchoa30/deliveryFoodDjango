from django import forms
from ..models import Customer

class FormCustomer(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'last_name', 'phone_number', 'address']
        labels = {
            'name': 'Nombre',
            'last_name': 'Apellido',
            'phone_number': 'Número de teléfono',
            'address': 'Dirección',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        if not name.isalpha():
            raise forms.ValidationError('El nombre solo puede contener letras.')
        return name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name'].strip()
        if not last_name.isalpha():
            raise forms.ValidationError('El apellido solo puede contener letras.')
        return last_name

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number'].strip()
        if not phone_number.isdigit():
            raise forms.ValidationError('El número de teléfono solo puede contener números.')
        if len(phone_number) < 7 or len(phone_number) > 15:
            raise forms.ValidationError('El número de teléfono debe tener entre 7 y 15 dígitos.')
        return phone_number

    def clean_address(self):
        address = self.cleaned_data['address'].strip()
        if len(address) < 5:
            raise forms.ValidationError('La dirección debe tener al menos 5 caracteres.')
        return address

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        last_name = cleaned_data.get('last_name')
        phone_number = cleaned_data.get('phone_number')
        address = cleaned_data.get('address')
        
        if not name or not last_name or not phone_number or not address:
            raise forms.ValidationError('Todos los campos son obligatorios.')
        
        return cleaned_data

    def save(self, commit=True):
        customer = super().save(commit=False)
        if commit:
            customer.save()
        return customer
