from django.contrib import admin

from .models import Customer, Networks


class CustomerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Customer, CustomerAdmin)


class NetworksAdmin(admin.ModelAdmin):
    pass


admin.site.register(Networks, NetworksAdmin)
