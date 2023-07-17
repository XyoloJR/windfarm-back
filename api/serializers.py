from __future__ import annotations

from rest_framework.serializers import ModelSerializer, SerializerMethodField
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


def tree_item_representation(item: ElectricityMeter | WindTurbine | WindFarm) -> dict:
    return {
        'id': item.__repr__(),
        'type': item.__class__.__name__,
        'name': item.__str__(),
        'children': []
    }


class WindFarmTreeSerializer(ModelSerializer):
    class Meta:
        model = WindFarm

    def to_representation(self, farm: WindFarm):
        farm_representation = tree_item_representation(farm)
        if farm.turbines.exists():
            farm_representation['children'].append({
                'id': None,
                'type': 'Group',
                'name': 'Éoliennes',
                'children': [
                    tree_item_representation(t)
                    for t in farm.turbines.all()
                ]
            })
        farm_representation['children'].append(tree_item_representation(farm.electricity_meter))

        return farm_representation


class WindTurbineModelSerializer(ModelSerializer):
    class Meta:
        model = WindTurbineModel
        fields = '__all__'


class WindTurbineSerializer(ModelSerializer):
    class Meta:
        model = WindTurbine
        fields = '__all__'
