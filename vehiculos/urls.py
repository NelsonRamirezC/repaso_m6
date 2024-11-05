from django.urls import path
from . import views

urlpatterns = [
    path('', views.VehiculosView.as_view(), name='lista_vehiculos'),
]



