from django.contrib import admin
from django.urls import path
from rest_framework import routers

from customer.views import CustomerViewSet

customer_router = routers.SimpleRouter()
customer_router.register(r'customer', CustomerViewSet, basename="customer")

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += customer_router.urls
