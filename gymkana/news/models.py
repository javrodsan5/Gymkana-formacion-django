from django.db import models
from django.utils import timezone

class BaseItems(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    body = models.TextField()

class New(BaseItems):
    publish_date = models.DateField()
    image = models.ImageField(upload_to='news', default='new.png')

    def __str__(self):
        return self.title
