from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Vehiculo

class VehiculosView(ListView):
    model = Vehiculo
    template_name = "vehiculos/vehiculos.html"
    context_object_name = 'vehiculos'