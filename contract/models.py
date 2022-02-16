from django.db import models
from django.conf import settings

from customer.models import Customer


class Contract(models.Model):
    STATUS = {
        ("Dr", "Draft"),
        ("SC", "Send to customer"),
        ("OK", "Signed")
    }

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=False,
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        blank=False,
    )

    signed = models.BooleanField(default=False, blank=False,)
    status = models.CharField(choices=STATUS, default="Dr", max_length=2, blank=False,)
    description = models.TextField(blank=True,)
    creation_date = models.DateTimeField(auto_now_add=True, blank=False)
    signed_date = models.DateTimeField(blank=True)
    price = models.IntegerField(blank=False)
