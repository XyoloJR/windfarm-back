from rest_framework.generics import RetrieveAPIView
from .models import (
    ElectricityMeter,
    WindFarm,
    WindTurbineModel,
    WindTurbine,
)
from .serializers import (
    ElectricityMeterSerializer,
    WindFarmSerializer,
    WindTurbineModelSerializer,
    WindTurbineSerializer,
)


class RetrieveElectricityMeter(RetrieveAPIView):
    queryset = ElectricityMeter.objects.all()
    serializer_class = ElectricityMeterSerializer


class RetrieveWindFarm(RetrieveAPIView):
    queryset = WindFarm.objects.all()
    serializer_class = WindFarmSerializer


class RetrieveWindTurbineModel(RetrieveAPIView):
    queryset = WindTurbineModel.objects.all()
    serializer_class = WindTurbineModelSerializer


class RetrieveWindTurbine(RetrieveAPIView):
    queryset = WindTurbine.objects.all()
    serializer_class = WindTurbineSerializer
