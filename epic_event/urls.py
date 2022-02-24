from django.contrib import admin
from django.urls import path
from rest_framework import routers

from customer.views import CustomerViewSet
from conversion.views import ConversionViewSet
from event.views import EventViewSet
from contract.views import ContractViewSet

customer_router = routers.SimpleRouter()
customer_router.register(r'customer', CustomerViewSet, basename="customer")

conversion_router = routers.SimpleRouter()
conversion_router.register(r'conversion', ConversionViewSet, basename="conversion")

event_router = routers.SimpleRouter()
event_router.register(r'event', EventViewSet, basename="event")

contract_router = routers.SimpleRouter()
contract_router.register(r'contract', ContractViewSet, basename="contract")

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += customer_router.urls
urlpatterns += conversion_router.urls
urlpatterns += event_router.urls
urlpatterns += contract_router.urls
