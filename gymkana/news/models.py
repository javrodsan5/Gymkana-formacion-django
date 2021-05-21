from django.db import models

class BaseItems(models.Model):
    title = models.CharField(max_length=20, blank=False)
    subtitle = models.CharField(max_length=20, blank=False)
    body = models.TextField(blank=False)

class New(BaseItems):
    publish_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', default='/static/news/images/new.png')

    def __str__(self):
        return self.title
