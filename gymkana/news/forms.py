from django import forms

class NewForm(forms.Form):
    title = forms.CharField(label='Título', max_length=20)
    subtitle = forms.CharField(label='Subtítulo', max_length=20)
    body = forms.CharField(label='Cuerpo')
    image = forms.ImageField(label='Imagen de la noticia')