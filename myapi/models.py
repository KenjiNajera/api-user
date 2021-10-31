from django.db import models


# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=60)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    avatar = models.CharField(max_length=150)
    

class Empleado(models.Model):
    nombre= models.CharField(max_length=60)
    apellido=models.CharField(max_length=60)
    correo=models.CharField(max_length=60)
    fechaIngreso=models.DateField(auto_now_add=False)