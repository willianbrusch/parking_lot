from django.db import models


class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=255)
    license_plate = models.CharField(max_length=255)
    arrived_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(null=True)
    amount_paid = models.IntegerField(null=True)
    variety = models.CharField(max_length=255, null=True)
    level_name = models.CharField(max_length=255, null=True)
    level_id = models.CharField(max_length=255, null=True)
