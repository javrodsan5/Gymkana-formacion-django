from typing_extensions import Required
from django.db import models

class BaseItems(models.Model):
    title = models.CharField(required = True)
    subtitle = models.CharField(required = True)
    body = models.TextField(required = True)

class Event(BaseItems):
    start_date = models.DateField(required = True)
    end_date = models.DateField(required = True)