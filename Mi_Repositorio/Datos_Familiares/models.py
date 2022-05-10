from django.db import models


class Padre(models.Model):
    nombre= models.CharField(max_length= 30)
    Edad= models.IntegerField()
    color_favorito= models.CharField(max_length=30)
    fecha_de_nacimiento= models.DateField()

class Madre(models.Model):
    nombre= models.CharField(max_length= 30)
    Edad= models.IntegerField()
    color_favorito= models.CharField(max_length= 30)
    fecha_de_nacimiento= models.DateField()

class Hermana(models.Model):
    nombre= models.CharField(max_length= 30)
    Edad= models.IntegerField()
    color_favorito= models.CharField(max_length= 30)
    fecha_de_nacimiento= models.DateField()

class Novia(models.Model):
    nombre= models.CharField(max_length= 30)
    Edad= models.IntegerField()
    color_favorito= models.CharField(max_length= 30)
    fecha_de_nacimiento= models.DateField()
