from django import forms


class ArticleForm(forms.Form):
    titulo = forms.CharField()
    descripcion = forms.CharField(widget=forms.Textarea)
