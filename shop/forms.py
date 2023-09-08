from django import forms

from shop.models import Product, Version


class ProductForm(forms.ModelForm):

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Product
        #fields = '__all__'
        exclude = ('date_creation', 'date_change', )

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        invalid_names = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for invalid_name in invalid_names:
            if invalid_name == cleaned_data:
                raise forms.ValidationError(f'Ошибка, связанная с наименованием "{invalid_name}"')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        invalid_descriptions = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for invalid_description in invalid_descriptions:
            if invalid_description in cleaned_data:
                raise forms.ValidationError(f'Ошибка, связанная с описанием "{invalid_description}"')

        return cleaned_data


class VersionForm(forms.ModelForm):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Version
        fields = '__all__'