from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .views import (
    RetrieveElectricityMeter,
    RetrieveWindFarm,
    RetrieveWindTurbineModel,
    RetrieveWindTurbine,
)

urlpatterns = [
    path('schema', SpectacularAPIView.as_view(), name='schema'),
    path('doc', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('electricity-meters/<int:pk>', RetrieveElectricityMeter.as_view()),
    path('wind-farms/<int:pk>', RetrieveWindFarm.as_view()),
    path('wind-turbine-models/<int:pk>', RetrieveWindTurbineModel.as_view()),
    path('wind-turbines/<int:pk>', RetrieveWindTurbine.as_view())
]
