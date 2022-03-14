from django.db import models


class Customer(models.Model):
    CUSTOMER_STATUS = {
        ("lead", "Lead"),
        ("acti", "Active"),
        ("anon", "Anonymized"),
    }

    company_name = models.CharField(max_length=50, blank=False)
    status = models.CharField(choices=CUSTOMER_STATUS, max_length=4, blank=False)
    mailing_address = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.company_name


class Networks(models.Model):
    NETWORK_NAME = {
        ("FB", "Facebook"),
        ("TW", "Twitter"),
        ("LI", "Linkedin"),
    }

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=False)
    name = models.CharField(choices=NETWORK_NAME, max_length=2, blank=False)
    username = models.CharField(max_length=200, blank=False)

    class Meta:
        verbose_name_plural = "Networks"
