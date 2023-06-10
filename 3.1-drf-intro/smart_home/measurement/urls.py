from django.urls import path

from measurement.views import SensorsView, MeasurementsInput, aSensorView

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', aSensorView.as_view()),
    path('measurements/', MeasurementsInput.as_view()),
]
