from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from empresas.models import Shop


class Client (models.Model):
    phone = models.BigIntegerField()
    address = models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name="Cliente"
        verbose_name_plural = "Clientes"
    def __str__(self):
        return self.user.username

class Staff (models.Model):
    phone = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop , on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    send_notification = models.CharField(max_length=255)
    class Meta:
        verbose_name = "Personal"
        verbose_name_plural = "Personal"
    def __str__(self):
        return self.type