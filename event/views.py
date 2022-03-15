from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoObjectPermissions, IsAuthenticated
from drf_roles.mixins import RoleViewSetMixin
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import EventSerializer
from .models import Event


class EventViewSet(RoleViewSetMixin, ModelViewSet):
    model = Event
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'assigned_user', 'contract__customer',
                        'contract__customer__company_name', 'start_date', 'end_date']

    def get_queryset_for_admins(self) -> object:
        return Event.objects.all()

    def get_queryset_for_managements(self) -> object:
        return Event.objects.all()

    def get_queryset_for_sales(self):
        return Event.objects.all()

    def get_queryset_for_supports(self):
        return Event.objects.filter(assigned_user=self.request.user).distinct()
