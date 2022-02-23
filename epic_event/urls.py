from django.contrib import admin
from django.urls import path
from rest_framework import routers

from customer.views import CustomerViewSet
from conversion.views import ConversionViewSet

customer_router = routers.SimpleRouter()
customer_router.register(r'customer', CustomerViewSet, basename="customer")

conversion_router = routers.SimpleRouter()
conversion_router.register(r'conversion', ConversionViewSet, basename="conversion")

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += customer_router.urls
urlpatterns += conversion_router.urls
