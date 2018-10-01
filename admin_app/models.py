from django.db.models import ForeignKey
from django.db.models.functions import datetime
from django.shortcuts import render

# Create your views here.
from django.db import models

class Tipo_Recurso(models.Model):
    nombre = models.CharField(max_length=50, null=False)

class Estado(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=50, null=False)

class Rol(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=50, null=False)

class Responsable(models.Model):
    nombres = models.CharField(max_length=50, null=False)
    apellidos = models.CharField(max_length=50, null=False)
    usuario = models.CharField(max_length=50, null=False)
    rol = ForeignKey(Rol)

class Recurso(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=100, null=False)
    tipoRecurso = ForeignKey(Tipo_Recurso)
    idSolicitud = models.CharField(max_length=50, null=False)
    idProyecto = models.CharField(max_length=50, null=False)
    descripcionSolicitud = models.CharField(max_length=300, null=False)
    fechaEntrega = models.DateField(default=datetime.now, blank=True)
    presupuesto = models.DecimalField(default=datetime.now, blank=True)
    estado = ForeignKey(Estado)

class Recurso_Responsable(models.Model):
    responsable = ForeignKey(Responsable)
    rescursos = ForeignKey(Recurso)

class Recurso_Intermedio(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    tipoRecurso = ForeignKey(Tipo_Recurso)
    estado = ForeignKey(Estado)
    descripcion = models.CharField(max_length=200, null=False)
    recursoPrincipal = ForeignKey(Recurso)
    responsable = ForeignKey(Responsable)

class Lista_Chequeo(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=200, null=False)
    asignado = ForeignKey(Responsable)

class Resultado_ListaChequeo(models.Model):
    recurso = ForeignKey(Recurso_Intermedio)
    itemChequeo = ForeignKey(Lista_Chequeo)
    resultado = models.BooleanField()