# Generated by Django 5.1.3 on 2024-11-05 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0002_vehiculo_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='create_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]