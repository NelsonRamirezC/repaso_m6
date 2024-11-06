from django.db import models

class Vehiculo(models.Model):
    tipo_vehiculo = [
        ('Pasajeros', 'Pasajeros'),
        ('Carga', 'Carga'),
        ('Deportivo', 'Deportivo'),
    ]
    
    marca = models.CharField(max_length=100, blank=False, null=False)
    modelo = models.CharField(max_length=100, blank=False, null=False)
    tipo = models.CharField(max_length=50, blank=False, null=False, choices=tipo_vehiculo, default='Pasajeros')
    create_at = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    update_at = models.DateTimeField(null=False, blank=False, auto_now_add=False, auto_now=True)
    imagen = models.ImageField(upload_to='vehiculos/', blank=True, null=True)
    
    
    def __str__(self) -> str:
        return f"Marca: {self.marca} - Modelo: {self.modelo}"
    
    class Meta:
        permissions = [("can_edit_vehiculos", "Puede agregar, visualizar, modificar vehículos (no puede eliminar)")]
        ordering = ['-update_at']