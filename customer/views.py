from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoObjectPermissions, IsAuthenticated
from drf_roles.mixins import RoleViewSetMixin
from rest_framework_extensions.routers import NestedRouterMixin
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CustomerSerializer, NetworksSerializer
from .models import Customer, Networks


class CustomerViewSet(NestedRouterMixin, RoleViewSetMixin, ModelViewSet):
    model = Customer
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'email', 'company_name']

    def get_queryset_for_admins(self):
        return Customer.objects.all()

    def get_queryset_for_managements(self):
        return Customer.objects.all()

    def get_queryset_for_sales(self):
        return Customer.objects.all()

    def get_queryset_for_supports(self):
        return Customer.objects.filter(customer__event__assigned_user=self.request.user).distinct()


class NetworksViewSet(NestedRouterMixin, RoleViewSetMixin, ModelViewSet):
    model = Networks
    serializer_class = NetworksSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

    def get_queryset_for_admins(self) -> object:
        return Networks.objects.all()

    def get_queryset_for_managements(self) -> object:
        return Networks.objects.all()

    def get_queryset_for_sales(self):
        return Networks.objects.all()

    def get_queryset_for_supports(self):
        return Networks.objects.filter(contract__event__assigned_user=self.request.user).distinct()
