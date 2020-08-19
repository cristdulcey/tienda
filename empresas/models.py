from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from geoposition.fields import GeopositionField


class Shop(models.Model):
    name=models.CharField(max_length=255)
    nit=models.BigIntegerField()
    address=models.CharField(max_length=255)
    phone=models.BigIntegerField()
    logo=models.ImageField(upload_to="shop_image", null=True, blank=True)
    description=models.TextField(max_length=255)
    state=models.BooleanField(default=True)
    position = GeopositionField()

    class Meta:
        verbose_name="Tienda"
        verbose_name_plural="Tiendas"
    def __str__(self):
        return self.name


class Client(models.Model):
    phone = models.BigIntegerField()
    address = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.user.username

    def get_full_name_client(self):
        if self.user.get_full_name() == None or self.user.get_full_name() == "":
            return "no tiene nombre"
        else:
            return self.user.get_full_name()

    get_full_name_client.short_description = "Nombres"


class Staff(models.Model):
    phone = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    send_notification = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Personal"
        verbose_name_plural = "Personal"

    def __str__(self):
        return self.type