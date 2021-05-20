from django.db import models

class BaseItems(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    body = models.TextField()

class Event(BaseItems):
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title