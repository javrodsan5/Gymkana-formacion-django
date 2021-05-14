from django.contrib import admin

# Register your models here.
from .models import New

class NewAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Heading', {'fields': ['title','subtitle']}),
        ('Article body', {'fields': ['body', 'image']}),
        #('Date information', {'fields': ['publish_date']}),
    ]
    list_display = ('title', 'subtitle', 'publish_date')
    list_filter = ['publish_date']

admin.site.register(New, NewAdmin)