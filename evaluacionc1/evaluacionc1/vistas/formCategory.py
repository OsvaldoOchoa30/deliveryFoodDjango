from django import forms
from ..models import Category

class FormCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type']
        labels = {
            'name': 'Nombre de la categoría',
            'type': 'Tipo de categoría',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    def clean_name(self):
        name = self.cleaned_data['name']
        return name

    def clean_type(self):
        type = self.cleaned_data['type']
        return type

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        type = cleaned_data.get('type')
        if not name or not type:
            raise forms.ValidationError('Todos los campos son obligatorios.')
        return cleaned_data

    def save(self, commit=True):
        category = super().save(commit=False)
        if commit:
            category.save()
        return category
