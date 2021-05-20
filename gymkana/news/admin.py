from django.contrib import admin

from .models import New


class NewAdmin(admin.ModelAdmin):
    fields = ['title', 'subtitle', 'publish_date']

admin.site.register(New, NewAdmin)
