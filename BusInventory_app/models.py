from django.db import models

# Create your models here.



class Bus(models.Model):
    bus_number = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    number_of_seats = models.IntegerField()
    trip = models.CharField(max_length=100)
    trip_duration = models.CharField(max_length=50)
    conductor = models.CharField(max_length=100)
    driver = models.CharField(max_length=100)

    def __str__(self):
        return self.bus_number
