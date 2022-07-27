from random import choices
from typing import AbstractSet
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.files.storage import FileSystemStorage

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1,'Admin'),
        (2,'Bodeguero'),
        (3,'Residente de Obra')
    )
    user_type=models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,null=True)



class Obra(models.Model):
    choices_status=[('1','Pendiente'),('2','Finalizado'),('3','En proceso')]
    nombre=models.CharField(max_length=300)
    ubicacion=models.CharField(max_length=300)
    total_villas=models.IntegerField(null=True, default=0)
    status=models.CharField(max_length=50, choices=choices_status,default="En proceso")
    


class Villa(models.Model):
    identificador=models.CharField(max_length=20)
    obra=models.ForeignKey(Obra,to_field="id", on_delete=models.CASCADE,default=1)



class Bodega(models.Model):
    nombre=models.CharField(max_length=100)
    ubicacion=models.CharField(max_length=600)
    encargado=models.CharField(max_length=300)
    obra=models.ForeignKey(Obra,to_field="id", on_delete=models.CASCADE)


class BodegaProductos(models.Model):
    
    choices_categoria=[('1','EQUIPO'),('2','MUEBLE'),('3','ACCESORIO'),('4','HERRERIA'),('5','CANCELERIA'),('6','CARPINTERIA'),('7','ACABADO'),('8','MATERIAL')]
    choices_unidad=[('1','PIEZA'),('2','CUBETA'),('3','GALON'),('4','BULTO'),('5','m3'),('6','KG'),('7','TONELADA'),('8','MILLA'),('9','LITRO'),('10','JUEGO'),('11','LOTE'),('12','m2')]
    
    clave=models.CharField(max_length=30, unique=True,default="")
    categoria=models.CharField(max_length=80, choices=choices_categoria,default=0)
    unidad=models.CharField(max_length=80, choices=choices_unidad,default=0)
    descripcion = models.CharField(max_length=200,default="")
    proveedor = models.CharField(max_length=500,default="")
    bodega=models.ForeignKey(Bodega,to_field="id", on_delete=models.CASCADE)
    ubicacion=models.CharField(max_length=200, default="")
    cantidad=models.IntegerField(null=True, default=0)
    minimo=models.IntegerField(null=True,default=0)




class Insumos(models.Model):
    obra=models.ForeignKey(Obra,to_field="id",on_delete=models.CASCADE)
    villa=models.ForeignKey(Villa,to_field="id",on_delete=models.CASCADE)
    bodegaproducto=models.ForeignKey(BodegaProductos,to_field="id",on_delete=models.CASCADE,null=True)
    fecha=models.DateField("fecha_explosion_insumo")
    cantidad=models.IntegerField(null=True, default=0)
    notas=models.CharField(max_length=800,default='',null=True,blank=True)
    
class Solicitud(models.Model):
    solicitud=models.CharField(max_length=300)
    fecha=models.DateField("fecha_solicitud_requisicion")
    obra=models.ForeignKey(Obra,to_field="id", on_delete=models.CASCADE,default=1)
    solicita=models.CharField(max_length=300)
    bodegaproducto=models.ForeignKey(BodegaProductos,to_field="id",on_delete=models.CASCADE,default=1)
    descripcion=models.CharField(max_length=300,default="")
    unidad=models.CharField(max_length=300,default="")
    cantidad=models.IntegerField(null=True, default=0)
    
class Compra(models.Model):
    solicitud=models.ForeignKey(Solicitud,to_field="id",on_delete=models.CASCADE)
    compra=models.IntegerField(null=True, default=0)
    
class Recepcion(models.Model):
    solicitud=models.ForeignKey(Solicitud,to_field="id",on_delete=models.CASCADE)
    llegada=models.IntegerField(null=True, default=0)
    pendiente=models.IntegerField(null=True, default=0)
    utilizado=models.IntegerField(null=True, default=0)
    saldo=models.IntegerField(null=True, default=0)

fs = FileSystemStorage(location='app/upload')
class Archivos(models.Model):
    solicitud = models.CharField(max_length=3)
    fecha = models.DateField(auto_now_add=True)
    ruta = models.FileField(upload_to='xml/',max_length=100)
    