from django.contrib import admin

from .models import Customer, Networks


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'status')


admin.site.register(Customer, CustomerAdmin)


class NetworksAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'name')


admin.site.register(Networks, NetworksAdmin)
