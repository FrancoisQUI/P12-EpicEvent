from django.contrib import admin

from .models import Conversion


class ConversionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Conversion, ConversionAdmin)
