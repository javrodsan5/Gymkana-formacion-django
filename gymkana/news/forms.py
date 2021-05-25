from django.forms import ModelForm
from news.models import New
from django.core.exceptions import ValidationError


class NewForm(ModelForm):
    model = New
    fields = ['title', 'subtitle', 'body', 'image']

