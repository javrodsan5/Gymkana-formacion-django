from django.forms import ModelForm
from news.models import New
from django.core.exceptions import ValidationError
from django.db.models.fields.files import FileField, ImageFieldFile
from django.core.files.uploadedfile import InMemoryUploadedFile


class NewForm(ModelForm):
    class Meta:
        model = New
        fields = ['title', 'subtitle', 'body', 'image']

    def clean_image(self):
        image = self.cleaned_data.get('image', False)

        if isinstance(image, InMemoryUploadedFile) or isinstance(image, ImageFieldFile) or isinstance(image, str):
            return image
        else:
            if ("/png" not in image.content_type and "/jpg" not in image.content_type) or image.size > 10*1024*1024:
                raise ValidationError(
                    "Allowed extensions are: PNG and JPG. The image must be < 10MB")
            return image
