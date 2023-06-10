from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=250)
    

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurement')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
 
