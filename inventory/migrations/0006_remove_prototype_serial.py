# Generated by Django 5.1.6 on 2025-02-15 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_remove_prototype_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prototype',
            name='serial',
        ),
    ]
