# Generated by Django 5.1.6 on 2025-02-15 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_alter_brand_description_alter_brand_tipo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prototype',
            options={'verbose_name': 'Modelo', 'verbose_name_plural': 'Modelos'},
        ),
        migrations.AddField(
            model_name='prototype',
            name='tipo',
            field=models.CharField(blank=True, choices=[('A', 'PERIFERICOS'), ('B', 'EQUIPOS DE OFICINA'), ('C', 'EQUIPOS DE COMPUTO'), ('D', 'OTROS')], max_length=1, null=True, verbose_name='Tipo de marca'),
        ),
        migrations.AlterUniqueTogether(
            name='brand',
            unique_together={('description', 'tipo')},
        ),
    ]
