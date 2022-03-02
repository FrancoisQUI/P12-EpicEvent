from django.contrib import admin

from .models import Conversion


class ConversionAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'medium')


admin.site.register(Conversion, ConversionAdmin)
