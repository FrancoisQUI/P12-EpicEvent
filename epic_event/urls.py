from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_extensions.routers import ExtendedSimpleRouter

from customer.views import CustomerViewSet, NetworksViewSet
from conversion.views import ConversionViewSet
from event.views import EventViewSet
from contract.views import ContractViewSet

customer_router = ExtendedSimpleRouter()
customer_router.register(r'customer', CustomerViewSet, basename="customer")\
    .register(r'networks', NetworksViewSet, basename="networks", parents_query_lookups=['object_id'])

conversion_router = SimpleRouter()
conversion_router.register(r'conversion', ConversionViewSet, basename="conversion")

event_router = SimpleRouter()
event_router.register(r'event', EventViewSet, basename="event")

contract_router = SimpleRouter()
contract_router.register(r'contract', ContractViewSet, basename="contract")

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += customer_router.urls
urlpatterns += conversion_router.urls
urlpatterns += event_router.urls
urlpatterns += contract_router.urls
