from django.db import models

# Create your models here.
from django.utils.text import slugify


class Category (models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to = "image_categories")
    description = models.TextField()
    slug = models.CharField(max_length=250, blank=True, null=True)
    parent = models.CharField(max_length=250)

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
    description = models.TextField()
    class Meta:
        verbose_name="Unidad"
        verbose_name_plural = "Unidades"
    def __str__(self):
        return self.user.username


class Product (models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    description = models.TextField()
    valor = models.IntegerField()
    quantity = models.IntegerField()
    discount = models.IntegerField()
    # category = models.ManyToManyField(Category)
    # unidades = models.ManyToManyField(Unit)
    # shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    class Meta:
        verbose_name="Producto"
        verbose_name_plural = "Productos"
    def __str__(self):
        return self.user.username