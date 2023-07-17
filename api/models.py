from django.db import models


class WindFarm(models.Model):
    name = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    commissioning_date = models.DateTimeField(auto_now_add=True)


class WindTurbineModel(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    nominal_power = models.IntegerField()


class WindTurbine(models.Model):
    name = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    tower_height = models.IntegerField()
    model = models.ForeignKey(WindTurbineModel, related_name='known_turbines', on_delete=models.PROTECT)
    wind_farm = models.ForeignKey(WindFarm, related_name='turbines', on_delete=models.CASCADE)


class ElectricityMeter(models.Model):
    name = models.CharField(max_length=50)
    reference = models.CharField(max_length=50)
    wind_farm = models.OneToOneField(WindFarm, related_name='electricity_meter', on_delete=models.CASCADE)
    activation_date = models.DateTimeField(auto_now_add=True)
