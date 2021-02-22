from django.db import models


# class Spot(models.Model):
#     available_bike_spots = models.IntegerField()
#     available_car_spots = models.IntegerField()


class Level(models.Model):
    name = models.CharField(max_length=255)
    fill_priority = models.IntegerField()
    bike_spots = models.IntegerField()
    car_spots = models.IntegerField()

    def __str__(self):
        return f'{self.name}'
