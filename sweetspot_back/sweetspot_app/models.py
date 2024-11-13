from django.db import models

# Create your models here.
class Spot(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)  # Added address field
    latitude = models.FloatField()
    longitude = models.FloatField()
    capacity = models.IntegerField()
    
    def __str__(self):
        return self.name