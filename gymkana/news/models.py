from django.db import models

class BaseItem(models.Model):
    title = models.CharField(max_length=70)
    subtitle = models.CharField(max_length=100)
    body = models.TextField

    class Meta:
        abstract = True
        ordering = ['title']

class New(BaseItem):
    publish_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to ='uploads/images/% Y/% m/% d/', default='static/news/images/default-news.jpeg')