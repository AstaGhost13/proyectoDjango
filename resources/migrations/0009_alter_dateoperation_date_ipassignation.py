# Generated by Django 5.1.6 on 2025-02-15 22:57

import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_alter_brand_unique_together'),
        ('resources', '0008_dateoperation'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='dateoperation',
            name='date',
            field=models.DateField(verbose_name='Fecha del primer uso'),
        ),
        migrations.CreateModel(
            name='IpAssignation',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('ip', models.GenericIPAddressField(verbose_name='Dirección IP')),
                ('created_by', django_currentuser.db.models.fields.CurrentUserField(blank=True, default=django_currentuser.middleware.get_current_authenticated_user, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fk_ipassignation_product', to='inventory.product', verbose_name='Producto')),
                ('updated_by', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Asignación de IP',
                'verbose_name_plural': 'Asignación de IP',
                'db_table': 'tb_ipassignation',
            },
        ),
    ]
