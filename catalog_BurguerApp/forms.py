from django import forms
from .models import Products, Categories;

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'price', 'category', 'path', 'offer']
        offer = forms.BooleanField(
            required=False,
            widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
        )
        path = forms.URLField(
            required=False,
            widget=forms.URLInput(attrs={'class': 'form-control'}),
            label="URL da Imagem",
            help_text="Insira a URL de uma imagem externa para o produto"
        )

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['name', 'path'] 