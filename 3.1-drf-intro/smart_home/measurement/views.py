# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorInfoSerializer


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorInfoView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorInfoSerializer


class MeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request, *args, **kwargs):
        if request.data.get('sensor') is None or request.data.get('temperature') is None:
            return Response({'error': 'Необходимо внести "sensor" и "temperature"'})
        try:
            sensor = Sensor.objects.get(id=request.data.get('sensor'))
            mes = Measurement.objects.create(temperature=request.data.get('temperature'),
                                             sensor=sensor,
                                             )
            return Response(
                            {'sensor': mes.sensor.id,
                             'temperature': mes.temperature,
                             'created_at': mes.created_at}
                            )
        except ObjectDoesNotExist:
            return Response({'error': 'Датчика нет в базе данных'})

# class SensorChangeView(CreateAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorSerializer
#
#     def post(self, request, *args, **kwargs):
#         if request.data.get('name') is None or request.data.get('description') is None:
#             return Response({'error': 'Необходимо внести "name" и "description"'})
#         else:
#             sen = Sensor.objects.create(name=request.data.get('name'),
#                                         description = request.data.get('description')
#                                              )
#             return Response(
#                             {
#                              'name': sen.name,
#                              'description': sen.description}
#                             )
