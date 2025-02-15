from django import forms
from django.db import models
from django.core.exceptions import ValidationError
from django_currentuser.db.models import CurrentUserField
from django.utils.translation import gettext_lazy as _
import uuid

from inventory.enums.tipo_marca import TipoMarca
from myapp.models import Custodiam

# Create your models here.


class Brand(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    created_by = CurrentUserField(
        related_name="%(class)s_created_by", null=True, blank=True, editable=False
    )
    updated_by = CurrentUserField(
        on_update=True,
        related_name="%(class)s_updated_by",
        null=True,
        blank=True,
        editable=False,
    )
    # Validacion en caso de que ya exista el registro
    # unique=True
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    description = models.CharField(
        max_length=5000,
        blank=False,
        null=False,
        verbose_name="Descripción",
    )
    
    tipo = models.CharField(
        max_length=1,
        choices=TipoMarca.OPCIONES,  # Usa las opciones de la clase
        blank=True,
        null=True,
        verbose_name=_("Tipo"),
    )
    
    # Prueba para el formulario
    def get_description(self):
        return f"{self.description} ({dict(TipoMarca.OPCIONES).get(self.tipo)})"
    
    def clean(self):
        # Convertir la descripción a mayúsculas
        self.description = self.description.upper()

        # Verificar si la descripción ya existe en el mismo tipo
        if self.tipo:  # Avoid the check if tipo is not selected.
            if Brand.objects.filter(description=self.description, tipo=self.tipo).exclude(pk=self.pk).exists():
                raise ValidationError({
                    'description': f'La descripción "{self.description}" ya existe para el tipo "{dict(TipoMarca.OPCIONES).get(self.tipo)}".'
                })
        super().clean()  # Always call super().clean()

        
    def __str__(self):
        return f"{self.description}"

    def save(self, *args, **kwargs):
            # Convertir la descripción a mayúsculas antes de validar
        self.description = self.description.upper()
        palabras_descripcion = self.description.split()
        marcas_predefinidas = {
                nombre.upper(): codigo for codigo, nombre in TipoMarca.OPCIONES
            }
        # Verificar palabra por palabra
        if not self.tipo:  
            for palabra in palabras_descripcion:
                if palabra in marcas_predefinidas:
                    self.tipo = marcas_predefinidas[palabra]
                    break
            else:
                self.tipo = TipoMarca.OTROS

        # Validar antes de guardar
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Marcas"
        db_table = "tb_brand"
        verbose_name = "Marca"
        unique_together = ('description', 'tipo') # Add this line


class Prototype(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    created_by = CurrentUserField(
        related_name="%(class)s_created_by", null=True, blank=True, editable=False
    )
    updated_by = CurrentUserField(
        on_update=True,
        related_name="%(class)s_updated_by",
        null=True,
        blank=True,
        editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.BooleanField(default=True)

    description = models.CharField(
        max_length=5000,
        blank=False,
        null=False,
        verbose_name="Descripción",
        unique=True,
    )
    brand = models.ForeignKey(
        Brand,
        verbose_name="Marca",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="fk_prototype_brand",
    )

    def __str__(self):
        return f"{self.description}"

    class Meta:
        verbose_name_plural = "Modelo"
        db_table = "tb_prototype"
        verbose_name = "Modelos"


class Product(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    created_by = CurrentUserField(
        related_name="%(class)s_created_by", null=True, blank=True, editable=False
    )
    updated_by = CurrentUserField(
        on_update=True,
        related_name="%(class)s_updated_by",
        null=True,
        blank=True,
        editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.BooleanField(default=True)
    description = models.CharField(
        max_length=5000,
        blank=False,
        null=False,
        verbose_name="Descripción",
        unique=True,
    )
    serie = models.CharField(
        max_length=5000, blank=False, null=False, verbose_name="Serie", unique=True
    )
    prototype = models.ForeignKey(
        Prototype,
        verbose_name="Modelo",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="fk_product_prototype",
    )

    def __str__(self):
        return f"{self.description}"

    class Meta:
        verbose_name_plural = "Producto"
        db_table = "tb_product"
        verbose_name = "Productos"


class AsignacionProduct(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    created_by = CurrentUserField(
        related_name="%(class)s_created_by", null=True, blank=True, editable=False
    )
    updated_by = CurrentUserField(
        on_update=True,
        related_name="%(class)s_updated_by",
        null=True,
        blank=True,
        editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.BooleanField(default=True)
    product = models.ForeignKey(
        Product,
        verbose_name="Producto",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="fk_asignacionproduct_product",
    )
    custodiam = models.ForeignKey(
        Custodiam,
        verbose_name="Custodiam",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="fk_asignacionproduct_custodiam",
    )

    def __str__(self):
        return f"{self.product}"

    class Meta:
        verbose_name_plural = "Asignación de Productos"
        db_table = "tb_asignacion_product"
        verbose_name = "Asignación de Productos"
