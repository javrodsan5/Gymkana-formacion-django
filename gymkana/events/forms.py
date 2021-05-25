from django.forms import ModelForm
from .models import Event
from django.core.exceptions import ValidationError


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'subtitle', 'body', 'start_date', 'end_date']