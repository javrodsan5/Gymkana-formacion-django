from typing import Optional
from django.db import models
from django.utils import timezone

class BaseItems(models.Model):
    title = models.CharField(required = True)
    subtitle = models.CharField(required = True)
    body = models.TextField(required = True)

class New(BaseItems):
    publish_date = models.DateField(timezone.now)
    image = models.ImageField()
