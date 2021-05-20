from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    fields = ['title', 'subtitle', 'start_date', 'end_date']

admin.site.register(Event, EventAdmin)
