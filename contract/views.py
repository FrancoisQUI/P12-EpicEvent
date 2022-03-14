from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoObjectPermissions, IsAuthenticated
from drf_roles.mixins import RoleViewSetMixin
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ContractSerializer
from .models import Contract


class ContractViewSet(RoleViewSetMixin, ModelViewSet):
    model = Contract
    serializer_class = ContractSerializer
    permission_classes = [DjangoObjectPermissions, IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'signed', 'author', 'customer']

    def get_queryset_for_admin(self):
        return Contract.objects.all()

    def get_queryset_for_management(self):
        return Contract.objects.all()

    def get_queryset_for_sales(self):
        return Contract.objects.all()

    def get_queryset_for_support(self):
        return Contract.objects.filter()

