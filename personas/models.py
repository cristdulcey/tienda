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