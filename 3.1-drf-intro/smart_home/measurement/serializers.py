from rest_framework import serializers
from measurement.models import Sensor, Measurement

# TODO: опишите необходимые сериализаторы
class SensorsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id','name','description']
        
class MeasurementSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature','created_at']
        
class aSensorSerialiser(serializers.ModelSerializer):
    measurements = MeasurementSerialiser(read_only=True, many=True)
    
    class Meta:
        model = Sensor
        fields = ['id','name','description', 'measurements']