from django.db import models

class BaseItems(models.Model):
    title = models.CharField(max_length=20, blank=False)
    subtitle = models.CharField(max_length=20, blank=False)
    body = models.TextField(blank=False)

class Event(BaseItems):
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)

    def __str__(self):
        return self.title