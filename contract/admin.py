from django.contrib import admin

from .models import Contract


class ContractAdmin(admin.ModelAdmin):
    list_display = ("customer", "status", "creation_date")


admin.site.register(Contract, ContractAdmin)
