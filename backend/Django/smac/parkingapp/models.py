from django.db import models

# Create your models here.

class ParkingState(models.Model):
    location = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    class Meta:
        db_table='parks'