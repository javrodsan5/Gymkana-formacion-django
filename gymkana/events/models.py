from django.db import models
from news.models import BaseItem

# Create your models here.
class Event(BaseItem):
    start_date = models.DateField()
    end_date = models.DateField()