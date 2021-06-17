from django.forms import ModelForm
from .models import Articulo
from django import forms

# class AddArticleForm(ModelForm):
#   class Meta:
#     model = Articulo
#     fields = '__all__'
#     # fields = ['titulo']

class AddArticleForm(forms.Form):
  titulo = forms.CharField(max_length=20)
  descripcion = forms.CharField(max_length=50)
  