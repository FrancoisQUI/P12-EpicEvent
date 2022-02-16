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
        on_delete=models.CASCADE
    )
    contract = models.ForeignKey(
        Contract,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=50)
    status = models.CharField(max_length=2, choices=STATUS)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
