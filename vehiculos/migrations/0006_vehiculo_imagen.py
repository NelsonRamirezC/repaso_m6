# Generated by Django 5.1.3 on 2024-11-06 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0005_alter_vehiculo_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='vehiculos/'),
        ),
    ]
