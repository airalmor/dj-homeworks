

from django.urls import path
from measurement.views import SensorsView, SensorInfoView, MeasurementView

urlpatterns = [
    path('sensors/<pk>/', SensorInfoView.as_view()),
    path('sensors/', SensorsView.as_view()),
    path('measurements/', MeasurementView.as_view())
]