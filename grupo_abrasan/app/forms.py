from dataclasses import fields
from tkinter import Widget
from django import forms
from pkg_resources import require
from .models import *

from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
    username=forms.CharField(label='Username',widget=forms.TextInput)
    password1=forms.CharField(label='Contraseña',widget=forms.TextInput)
    password2=forms.CharField(label='Confirma Contraseña',widget=forms.PasswordInput)
    user_type=forms.Select(attrs={'id':'user_type','name':'user_type','placeholder':'Tipo de Usuario'})
    class Meta:
        model=CustomUser
        fields=('username','password1','password2','user_type')+UserCreationForm.Meta.fields
        help_texts={k:"" for k in fields}


class BodegaForm(forms.ModelForm):
        class Meta: 
            model=Bodega
            fields='__all__'
            labels={
                'nombre':'Nombre',
                'ubicacion':'Ubicación',
                'encargado':'Encargado',
               
            }
            widgets={
                'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre bodega','id':'bodega','name':'bodega','for':'nombre','required':True}),
                'ubicacion':forms.TextInput(attrs={'class':'form-control','id':'ubicacion','for':'ubicacion','name':'ubicacion','required':True}),
                'encargado':forms.TextInput(attrs={'class':'form-control','id':'encargado','name':'encargado','for':'encargado','required':True}),
                
                
                
                
            }
class ObraForm(forms.ModelForm):
        class Meta: 
            model=Obra
            fields='__all__'
            labels={
                'nombre':'Nombre',
                'ubicacion':'Ubicación',
                'status':'Status',
                'total_villas':'Total Villas'
            }
            widgets={
                'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre Obra','id':'obra','name':'obra','for':'obra','required':True}),
                'ubicacion':forms.TextInput(attrs={'class':'form-control','id':'ubicacion','for':'ubicacion','name':'ubicacion','required':True}),
                'total_villas':forms.TextInput(attrs={'class':'form-control','id':'total','name':'total','for':'total','required':True}),
                'status':forms.Select(attrs={'class':'form-control','id':'total','name':'total','for':'total','required':True})
                
                
                
            }

class BodegaProducto(forms.ModelForm):
    class Meta: 
            model=BodegaProductos
            fields='__all__'
            labels={
                'cantidad':'Cantidad',
                'minimo':'Minimo',
                'ubicacion':'Ubicación',
                'descripcion':'Descripción',
                'unidad':'Unidad',
                'categoria':'Categoria',
                'proveedor':'Proveedor'
                
                
            }
            widgets={
                'proveedor':forms.TextInput(attrs={'class':'form-control','id':'proveedor','name':'proveedor','for':'proveedor','required':True}),
                'categoria':forms.Select(attrs={'class':'form-control','id':'cantegoria','name':'categoria','for':'categoria','required':True}),
                'unidad':forms.Select(attrs={'class':'form-control','id':'unidad','name':'unidad','for':'unidad','required':True}),
                'descripcion':forms.TextInput(attrs={'class':'form-control','id':'descripcion','name':'descripcion','for':'descripcion','required':True}),
                'ubicacion':forms.TextInput(attrs={'class':'form-control','id':'ubicacion','name':'ubicacion','for':'ubicacion','required':True}),
                'cantidad':forms.TextInput(attrs={'class':'form-control','id':'cantidad','name':'cantidad','for':'cantidad','required':True}),
                'minimo':forms.TextInput(attrs={'class':'form-control','id':'minimo','name':'minimo','for':'minimo','required':True}),
                'ubicacion':forms.TextInput(attrs={'class':'form-control','placeholder':'Ubicacion','id':'ubicacion','for':'ubicacion','name':'ubicacion','required':True}),
                
                
                
            }
    
    
class VillaForm(forms.ModelForm):
    class Meta: 
            model=Villa
            fields='__all__'
            labels={
                'identificador':'Identificador',
                'calle':'Calle',
                
            }
            widgets={
                'identificador':forms.TextInput(attrs={'class':'form-control','id':'identificador','name':'indentificador','for':'identificador','required':True}),
                
                
                
            }

class InsumosForm(forms.ModelForm):
    class Meta: 
            model=Insumos
            fields='__all__'
            
            
            
class SolicitudForm(forms.ModelForm):
    class Meta:
        model=Solicitud
        fields='__all__'
    
class CompraForm(forms.ModelForm):
    class Meta:
        model=Compra
        fields='__all__'
        labels={
                'compra':'compra',
            }
        widgets={
                'compra':forms.TextInput(attrs={'class':'form-control','id':'compra','name':'compra','for':'compra','required':True}),
                
                
        }

class RecepcionForm(forms.ModelForm):
    class Meta:
        model=Recepcion
        fields='__all__'
        labels={
                'llegada':'llegada',
                'pendiente':'pendiente',
                'utilizado':'utilizado',
                'saldo':'saldo',
                
            }
        widgets={
                'llegada':forms.TextInput(attrs={'class':'form-control','id':'llegada','name':'llegada','for':'llegada','required':True}),
                'pendiente':forms.TextInput(attrs={'class':'form-control','id':'pendiente','name':'pendiente','for':'pendiente','required':True}),
                'utilizado':forms.TextInput(attrs={'class':'form-control','id':'utilizado','name':'utilizado','for':'utilizado'}),
                'saldo':forms.TextInput(attrs={'class':'form-control','id':'saldo','name':'saldo','for':'saldo'}),
                
                
            }
            
class FileForm(forms.ModelForm):
    class Meta:
        model=Archivos
        fields='__all__'