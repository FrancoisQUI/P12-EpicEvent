from django.db import models


class Customer(models.Model):
    CUSTOMER_STATUS = {
        ("lead", "Lead"),
        ("acti", "Active"),
        ("anon", "Anonymized"),
    }

    company_name = models.CharField(max_length=50)
    status = models.CharField(choices=CUSTOMER_STATUS, max_length=4)
    mailing_address = models.CharField(max_length=200)
    email = models.CharField(max_length=100)


class Networks(models.Model):
    NETWORK_NAME = {
        ("FB", "Facebook"),
        ("TW", "Twitter"),
        ("LI", "Linkedin"),
    }

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(choices=NETWORK_NAME, max_length=2)
    username = models.CharField(max_length=200)

