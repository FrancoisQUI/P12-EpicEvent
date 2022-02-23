from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoObjectPermissions
from drf_roles.mixins import RoleViewSetMixin

from .serializers import EventSerializer
from .models import Event


class EventViewSet(RoleViewSetMixin, ModelViewSet):
    model = Event
    serializer_class = EventSerializer
    permission_classes = [DjangoObjectPermissions]

    def get_queryset_for_admin(self) -> object:
        return Event.objects.all()

    def get_queryset_for_management(self) -> object:
        return Event.objects.all()

    def get_queryset_for_sales(self):
        return Event.objects.all()

    def get_queryset_for_support(self):
        return Event.objects.filter(assigned_user=self.request.user).distinct()

    def get_queryset(self):
        return Event.objects.none()
