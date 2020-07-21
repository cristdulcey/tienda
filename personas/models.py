from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Client (models.Model):
    phone = models.BigIntegerField()
    address = models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name="Cliente"
        verbose_name_plural = "Clientes"
    def __str__(self):
        return self.user.username
class User (models.Model):
    username = models.CharField(max_length=255)
    firts_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    class Meta:
        verbose_name="Usuario"
        verbose_name_plural = "Usuarios"
    def __str__(self):
        return self.user.username
class Staff (models.Model):
    phone = models.BigIntegerField()
    user = models.(User, on_delete=models.CASCADE)
    id_shop = models.(Shop , on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    send_notification = models.CharField(max_length=255)
    class Meta:
        verbose_name = "Personal"
    def __str__(self):
        return self.Staff.type