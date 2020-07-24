from django.db import models

# Create your models here.
from empresas.models import Shop
from personas.models import Client, Staff
from productos.models import Category, Product


class Cupon(models.Model):
    name=models.CharField(max_length=255)
    code=models.BigIntegerField()
    percent=models.BigIntegerField()
    max_number=models.IntegerField()
    min_value=models.IntegerField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    class Meta:
        verbose_name="Cupon"
        verbose_name_plural = "Cupones"
    def __str__(self):
        return self.name

class Order(models.Model):
    date=models.DateField(auto_now=True, auto_now_add=False)
    value=models.IntegerField()
    state=models.BooleanField(default=True)
    client=models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        verbose_name="Orden"
        verbose_name_plural = "Ordenes"

    def __str__(self):
        return "{}".format(self.client)

class Notification (models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Notificacion"
        verbose_name_plural = "Notificaciones"

    def __str__(self):
        return "Id shop {}, Id staff {}, Id order {}".format(self.shop, self.staff, self.order)


class OrderProduct (models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    value_unit=models.BigIntegerField()
    value_total=models.BigIntegerField()

    class Meta:
        verbose_name = "Orden producto"
        verbose_name_plural = "Ordenes productos"

    def __str__(self):
        return self.quantity
