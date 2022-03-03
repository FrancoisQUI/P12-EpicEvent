from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "start_date", "assigned_user" )


admin.site.register(Event, EventAdmin)
