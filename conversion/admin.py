from django.contrib import admin

from .models import Conversion


class ConversionAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'medium', )
    list_filter = ('medium', 'customer', )


admin.site.register(Conversion, ConversionAdmin)
