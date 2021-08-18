from django.db import models

# Create your models here.

class ContainerState(models.Model):
    container_number=models.CharField(max_length=255)
    resource_weight=models.IntegerField(default=0)
    state=models.CharField(max_length=4)
    yard_location=models.CharField(max_length=3)
    booking_note=models.CharField(max_length=255)
    stack_location=models.CharField(max_length=255)
    start_time=models.DateTimeField()
    first_time=models.DateTimeField()
    second_time=models.DateTimeField()
    third_time=models.DateTimeField()
    complete_time=models.DateTimeField()