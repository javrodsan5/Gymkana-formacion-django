from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

class BaseItems(models.Model):
    title = models.CharField(max_length=20, blank=False)
    subtitle = models.CharField(max_length=20, blank=False)
    body = models.TextField(blank=False)

class Event(BaseItems):
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)

    def __str__(self):
        return self.title
    
    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError({'end_date': _('The end date must be after the start.')})
