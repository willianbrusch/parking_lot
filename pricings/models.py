from django.db import models


class Price(models.Model):
    a_coefficient = models.IntegerField()
    b_coefficient = models.IntegerField()
