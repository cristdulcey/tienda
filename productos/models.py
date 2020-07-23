from django.db import models
# Create your models here.
from django.utils.text import slugify
from empresas.models import Shop


class Category (models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to = "image_categories")
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, blank=True, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)

    class Meta:
        verbose_name="Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Unit (models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    class Meta:
        verbose_name="Unidad"
        verbose_name_plural = "Unidades"
    def __str__(self):
        return self.name


class Product (models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='foto_producto')
    description = models.TextField(blank=True)
    valor = models.IntegerField()
    quantity = models.IntegerField()
    discount = models.IntegerField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    unidades = models.ForeignKey(Unit, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    class Meta:
        verbose_name="Producto"
        verbose_name_plural = "Productos"
    def __str__(self):
        return self.name