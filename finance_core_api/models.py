from django.db import models


# Create your models here.
class Account(models.Model):
    id = models.UUIDField(max_length=10, primary_key=True)
    name = models.CharField(max_length=200)
    current_amount = models.DecimalField(decimal_places=2, max_digits=20)
    remain_amount = models.DecimalField(decimal_places=2, max_digits=20)


class Resource(models.Model):
    id = models.UUIDField(max_length=10, primary_key=True)
    name = models.CharField(max_length=200)
    total_amount = models.DecimalField(decimal_places=2, max_digits=20)
