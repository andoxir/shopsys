#coding:utf-8

from django import forms
from .models import Product


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []

    def clean_price(self):
        if self.cleaned_Data['price'] <= 0:
            return forms.ValidationError('price must over 0!')
        return self.cleaned_data['price']