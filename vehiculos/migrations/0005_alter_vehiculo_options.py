# Generated by Django 5.1.3 on 2024-11-05 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0004_alter_vehiculo_options_vehiculo_update_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'ordering': ['-update_at'], 'permissions': [('can_edit_vehiculos', 'Puede agregar, visualizar, modificar vehículos (no puede eliminar)')]},
        ),
    ]