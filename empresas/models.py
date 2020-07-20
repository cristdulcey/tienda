from django.db import models

# Create your models here.
class Shop(models.Model):
    name=models.CharField(max_length=255)
    nit=models.BigIntegerField()
    address=models.CharField(max_length=255)
    phone=models.BigIntegerField()
    logo=models.CharField(max_length=255)
    description=models.TextField(max_length=255)
    state=models.BooleanField(default=True)

    class Meta:
        verbose_name="Tienda"
        verbose_name_plural="Tiendas"
    def __str__(self):
        return self.name