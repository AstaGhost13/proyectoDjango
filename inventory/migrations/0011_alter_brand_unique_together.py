# Generated by Django 5.1.6 on 2025-02-15 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_alter_brand_description_alter_brand_tipo'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='brand',
            unique_together={('description', 'tipo')},
        ),
    ]
