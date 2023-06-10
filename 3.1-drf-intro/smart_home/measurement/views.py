from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorsSerialiser, MeasurementSerialiser, aSensorSerialiser


# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerialiser
    
    def post(self, request):
        name = request.data['name']
        description = request.data['description']
        new_sensor = Sensor.objects.create(name=name, description=description)
        
class MeasurementsInput(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerialiser
    
    def post(self, request):
        sensor = Sensor.objects.get(pk=request.data['sensor'])
        temperature = request.data['temperature']
        input = Measurement.objects.create(sensor=sensor,temperature=temperature)
    
class aSensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = aSensorSerialiser
    
    def patch(self, request, pk):
        sensor = Sensor.objects.get(pk=pk)
        if request.data.get('name'):
            sensor.name = request.data['name']
        if request.data.get('description'):
            sensor.description = request.data['description']   
        sensor.save()