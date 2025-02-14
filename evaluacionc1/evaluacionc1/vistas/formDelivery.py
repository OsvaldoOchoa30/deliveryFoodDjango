from django import forms
from ..models import Delivery

class FormDelivery(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['name', 'last_name', 'status', 'phone_number']
        labels = {
            'name': 'Nombre',
            'last_name': 'Apellido',
            'status': 'Estado de disponibilidad',
            'phone_number': 'Número de teléfono',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    def clean_name(self):
        name = self.cleaned_data['name'].strip()
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

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        last_name = cleaned_data.get('last_name')
        phone_number = cleaned_data.get('phone_number')

        if not name or not last_name or not phone_number:
            raise forms.ValidationError('Todos los campos son obligatorios.')
        
        return cleaned_data

    def save(self, commit=True):
        delivery = super().save(commit=False)
        if commit:
            delivery.save()
        return delivery
