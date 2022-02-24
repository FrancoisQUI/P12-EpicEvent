from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoObjectPermissions
from drf_roles.mixins import RoleViewSetMixin

from .serializers import ContractSerializer
from .models import Contract


class ContractViewSet(RoleViewSetMixin, ModelViewSet):
    model = Contract
    serializer_class = ContractSerializer
    permission_classes = [DjangoObjectPermissions]

    def get_queryset_for_admin(self) -> object:
        return Contract.objects.all()

    def get_queryset_for_management(self) -> object:
        return Contract.objects.all()

    def get_queryset_for_sales(self):
        return Contract.objects.all()

    def get_queryset_for_support(self):
        return Contract.objects.filter()

    def get_queryset(self):
        return Contract.objects.none()
