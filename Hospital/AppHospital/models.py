from django.db import models



class Medicos(models.Model):

    nombre = models.CharField(max_length= 40)
    apellido =  models.CharField(max_length=40)
    especialidad =  models.CharField(max_length=40)
    matricula =  models.IntegerField()


class Enfermeros(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    turno = models.CharField(max_length=40)
    n_empleado = models.IntegerField()

class Pacientes(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    fecha_ingreso = models.DateField()
    mail = models.EmailField()


