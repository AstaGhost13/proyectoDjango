# Generated by Django 5.1.6 on 2025-02-15 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_prototype_options_prototype_model_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prototype',
            name='model',
        ),
    ]
