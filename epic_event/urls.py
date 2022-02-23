from django.contrib import admin
from django.urls import path
from rest_framework import routers

from customer.views import CustomerViewSet
from conversion.views import ConversionViewSet
from event.views import EventViewSet

customer_router = routers.SimpleRouter()
customer_router.register(r'customer', CustomerViewSet, basename="customer")

conversion_router = routers.SimpleRouter()
conversion_router.register(r'conversion', ConversionViewSet, basename="conversion")

event_router = routers.SimpleRouter()
event_router.register(r'event', EventViewSet, basename="event")

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += customer_router.urls
urlpatterns += conversion_router.urls
urlpatterns += event_router.urls
