# Generated by Django 5.1.6 on 2025-02-15 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_asignacionproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='description',
            field=models.CharField(max_length=5000, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='tipo',
            field=models.CharField(blank=True, choices=[('A', 'PERIFERICOS'), ('B', 'EQUIPOS DE OFICINA'), ('C', 'EQUIPOS DE COMPUTO'), ('D', 'OTROS')], max_length=1, null=True, verbose_name='Tipo'),
        ),
    ]
