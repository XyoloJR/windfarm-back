from django.contrib import admin

from api.models import (
    WindFarm,
    WindTurbine,
    WindTurbineModel,
    ElectricityMeter,
)

admin.site.register(WindFarm)
admin.site.register(WindTurbine)
admin.site.register(WindTurbineModel)
admin.site.register(ElectricityMeter)
