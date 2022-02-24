from rest_framework import viewsets
from rest_framework.permissions import DjangoObjectPermissions, IsAuthenticated
from drf_roles.mixins import RoleViewSetMixin

from .serializers import CustomerSerializer, NetworksSerializer
from .models import Customer, Networks


class CustomerViewSet(RoleViewSetMixin, viewsets.ModelViewSet):
    model = Customer
    serializer_class = CustomerSerializer
    permission_classes = [DjangoObjectPermissions, IsAuthenticated]

    def get_queryset_for_admin(self) -> object:
        return Customer.objects.all()

    def get_queryset_for_management(self) -> object:
        return Customer.objects.all()

    def get_queryset_for_sales(self):
        return Customer.objects.all()

    def get_queryset_for_support(self):
        return Customer.objects.filter(contract__event__assigned_user=self.request.user).distinct()

    def get_queryset(self):
        return Customer.objects.none()


class NetworksViewSet(RoleViewSetMixin, viewsets.ModelViewSet):
    model = Networks
    serializer_class = NetworksSerializer
    permission_classes = [DjangoObjectPermissions]

    def get_queryset_for_admin(self) -> object:
        return Networks.objects.all()

    def get_queryset_for_management(self) -> object:
        return Networks.objects.all()

    def get_queryset_for_sales(self):
        return Networks.objects.all()

    def get_queryset_for_support(self):
        return Networks.objects.filter(contract__event__assigned_user=self.request.user).distinct()

    def get_queryset(self):
        return Networks.objects.none()
