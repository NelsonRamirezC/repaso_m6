# Generated by Django 5.1.3 on 2024-11-05 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='create_at',
            field=models.DateField(null=True),
        ),
    ]