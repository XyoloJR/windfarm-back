from rest_framework.serializers import ModelSerializer
from .models import (
    ElectricityMeter,
    WindFarm,
    WindTurbineModel,
    WindTurbine,
)


class ElectricityMeterSerializer(ModelSerializer):
    class Meta:
        model = ElectricityMeter
        fields = '__all__'


class WindFarmSerializer(ModelSerializer):
    class Meta:
        model = WindFarm
        fields = '__all__'


class WindTurbineModelSerializer(ModelSerializer):
    class Meta:
        model = WindTurbineModel
        fields = '__all__'


class WindTurbineSerializer(ModelSerializer):
    class Meta:
        model = WindTurbine
        fields = '__all__'
