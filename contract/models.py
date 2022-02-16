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
        on_delete=models.CASCADE
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )

    signed = models.BooleanField(default=False)
    status = models.CharField(choices=STATUS, default="Dr", max_length=2)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    signed_date = models.DateTimeField()
    price = models.IntegerField()
