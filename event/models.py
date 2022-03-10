from django.db import models
from django.conf import settings

from contract.models import Contract


class Event(models.Model):
    STATUS = {
        ("FE", "Future Event"),
        ("PE", "Pending Event"),
        ("OE", "Over Event"),
    }

    assigned_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=False,
    )
    contract = models.ForeignKey(
        Contract,
        on_delete=models.CASCADE,
        blank=False,
    )

    name = models.CharField(max_length=50, blank=False)
    status = models.CharField(max_length=2, choices=STATUS, blank=False, default="FE")
    description = models.TextField(blank=False)
    start_date = models.DateTimeField(blank=False)
    end_date = models.DateTimeField(blank=True, null=True)
