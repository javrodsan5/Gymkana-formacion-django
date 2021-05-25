from django.forms import ModelForm
from news.models import New
from django.core.exceptions import ValidationError


class NewForm(ModelForm):
    model = New
    fields = ['title', 'subtitle', 'body', 'image']

    def check_image_format(self):
        img = self.cleaned_data['image']
        if ".png" not in img:
            raise ValidationError("It must have the correct format")

        return img
