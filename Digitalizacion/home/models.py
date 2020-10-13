from django.db import models

# Create your models here.
class Verificador(models.Model):
    idVerificador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

class Preparador(models.Model):
    idPreparador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    idVerificador = models.ForeignKey(Verificador, on_delete=models.CASCADE)

class Estado(models.Model):
    idEstado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=20)

class Folio(models.Model):
    Folio = models.IntegerField(primary_key=True)
    tomos = models.CharField(max_length=100)
    oficios = models.CharField(max_length=10)
    referencia = models.CharField(max_length=10)
    idEstado = models.ForeignKey(Estado, on_delete=models.CASCADE)

class Digitalizador(models.Model):
    idDigitalizador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

class Paquete(models.Model):
    noPaquete = models.IntegerField(primary_key=True)
    folioInicio = models.IntegerField()
    folioFin = models.IntegerField()
    fechaExp = models.DateField()
    noFojas = models.IntegerField()
    recepcion = models.IntegerField()
    validacion = models.IntegerField()
    sellado = models.IntegerField()
    cosido = models.IntegerField()
    fechaRealizado = models.DateField

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=30)
    password = models.CharField(max_length=30)