from django import forms
from localflavor.us.forms import USStateField, USZipCodeField
from django.forms import ModelForm
from parler.forms import TranslatableModelForm

from shop.models import Product, Category


class AddProductForm(TranslatableModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title', 'description', 'price']

    def __init__(self, *args, **kwargs):
        super(AddProductForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class AddCategoryForm(TranslatableModelForm):
    class Meta:
        model = Category
        fields = ['title',]

    def __init__(self, *args, **kwargs):
        super(AddCategoryForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'


class EditProductForm(TranslatableModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title', 'description', 'price']

    def __init__(self, *args, **kwargs):
        super(EditProductForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
