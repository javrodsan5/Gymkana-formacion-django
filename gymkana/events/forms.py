from django.forms import ModelForm
from .models import Event
from django.core.exceptions import ValidationError


class EventForm(ModelForm):
    model = Event
    fields = ['title', 'subtitle', 'body', 'start_date', 'end_date']

    def check_end_after_start(self):
        
        cleaned_data = super().clean()
        end_date = cleaned_data.get("end_date")
        start_date = cleaned_data.get("start_date")
        if end_date and start_date:
            if end_date < start_date:
                msg = "The end must be after the start"
                self.add_error('start_date', msg)
                self.add_error('end_date', msg)