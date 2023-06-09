from django.contrib import admin

# Register your models here.
from measurement.models import Sensor, Measurement

class MeasurementInline(admin.TabularInline):
    model = Measurement
    extra = 1
    
@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id','name','description']
    list_filter = ['name','description']
    inlines = [MeasurementInline]
    
@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['id','sensor','temperature','created_at']
    list_filter = ['sensor','temperature','created_at']