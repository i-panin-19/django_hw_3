from django import forms

from shop.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        #fields = '__all__'
        exclude = ('date_creation', 'date_change', )