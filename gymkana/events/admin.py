from django.contrib import admin

from .models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'subtitle', 'body']}),
        ('Event information', {'fields': ['start_date', 'end_date']}),
    ]
    list_display = ('title', 'subtitle', 'start_date', 'end_date')

admin.site.register(Event, EventAdmin)