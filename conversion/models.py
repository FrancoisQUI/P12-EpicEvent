from django.db import models
from django.conf import settings

from customer.models import Customer


class Conversion(models.Model):
    MEDIUM = {
        ("SN", "Social Network"),
        ("eM", "Email"),
        ("pM", "Postal Mail"),
        ("PH", "Phoning"),
        ("FA", "Fair"),
    }

    assigned_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
    )

    medium = models.CharField(max_length=2, choices=MEDIUM)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    validate_date = models.DateTimeField()


