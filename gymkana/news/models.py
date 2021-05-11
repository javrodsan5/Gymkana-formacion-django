from django.db import models

class BaseItem(models.Model):
    title = models.CharField(max_length=70)
    subtitle = models.CharField(max_length=100)
    body = models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

    class Meta:
        abstract = True
        ordering = ['title']

class New(BaseItem):
    publish_date = models.DateTimeField('date published', auto_now_add=True)
    image = models.ImageField(upload_to ='uploads/images/', default='static/news/images/default-news.jpeg')