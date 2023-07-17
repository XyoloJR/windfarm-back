from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

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
    WindTurbineSerializer, WindFarmTreeSerializer,
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


class TreeView(APIView):
    def get(self, request):
        wind_farms = WindFarm.objects.all()
        serializer = WindFarmTreeSerializer(instance=wind_farms, many=True)
        return Response(serializer.data)
