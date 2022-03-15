from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoObjectPermissions, IsAuthenticated
from drf_roles.mixins import RoleViewSetMixin
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ConversionSerializer
from .models import Conversion


class ConversionViewSet(RoleViewSetMixin, ModelViewSet):
    model = Conversion
    serializer_class = ConversionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['medium', 'assigned_user', 'customer']

    def get_queryset_for_admins(self) -> object:
        return Conversion.objects.all()

    def get_queryset_for_managements(self) -> object:
        return Conversion.objects.all()

    def get_queryset_for_sales(self):
        return Conversion.objects.all()

    def get_queryset_for_supports(self):
        return Conversion.objects.none()
