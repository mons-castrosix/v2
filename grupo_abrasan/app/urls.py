from unicodedata import name
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView

from . import views
app_name="app"
urlpatterns=[
   #----------------- I N V E N T A R I O --------------------------------
   
   path("panel",views.panel, name="panel"),
   path("contra/",views.change_password,name='contra'),
   path("register/",views.register,name='register'),
   path("",LoginView.as_view(template_name="app/login.html"),name='login'),
   path("logout/",LogoutView.as_view(),name='logout'),
   
   #urls de acceso
    path("listar-inventario/",views.listar_inventario, name="listar_inventario"),
    path("agregar-producto/<bodega>", views.agregar_producto,name="agregar_producto"),
    path("modificar-producto/<id>/<bodega>", views.modificar_producto,name="modificar_producto"),

    
    
    #----------------- B O D E G A S --------------------------------------
    path("listar-bodegas/",views.listar_bodegas, name="listar_bodegas"),
    path("agregar-bodega/",views.agregar_bodega, name="agregar_bodega"),
    path("modificar-bodega/<id>/",views.modificar_bodega, name="modificar_bodega"),
    path("eliminar-bodega/<id>/",views.eliminar_bodega, name="eliminar_bodega"),
    
    #------------------ O B R A S ----------------------------------------
    path("listar-obras/",views.listar_obras, name="listar_obras"),
    path("agregar-obra/",views.agregar_obra, name="agregar_obra"),
    path("modificar-obra/<id>/",views.modificar_obra, name="modificar_obra"),
    path("eliminar-obra/<id>/",views.eliminar_obra, name="eliminar_obra"),
    
    #--------------- V I L L A S --------------------------------------------
    path("listar-villas/",views.listar_villas, name="listar_villas"),
    path("agregar-villa/",views.agregar_villa, name="agregar_villa"),
    path("modificar-villa/<id>/",views.modificar_villa, name="modificar_villa"),
    path("eliminar-villa/<id>/",views.eliminar_villa, name="eliminar_villa"),
    path("explosion-insumos/<id>/",views.explosion_insumos, name="explosion_insumos"),
    
    
    #------------- BODEGA OBRAS --------------------------------------------
   
   path("traspaso-bodega/<id>/<bodega>/<bp>",views.bodega_traspaso, name="traspaso"),
   path("listar-producto-bodega/<id>/",views.listar_productobodega,name="listar_productobodega"),
   path("eliminar-producto-bodega/<bodega>/<id>/",views.eliminar_productobodega,name="eliminar_productobodega"),
   path("agregar-a-villa/<bodega>/<id>/<bp>",views.villa_addproduct, name="villa_addproduct"),
   path("modificar-productobodega/<bodega>/<id>/<bp>",views.modificar_productobodega, name="modificar_prodcutobodega"),
  
   #------------------- SOLICITUD REQUISICION ---------------------------------
   path("solicitud-requisicion/<id>/",views.solicitud,name="solicitud_requisicion"),
   path("solicitudes/",views.solicitudes,name="listar_solicitudes"),
   path("eliminar-producto-solicitud/<id>",views.eliminar_prodsolicitud,name="eliminarprod_solicitud"),
   path("compras/<solicitud>",views.compra,name="compras"),
   path("modificar-compra/<id>/",views.modificar_compra,name="modificar_compra"),
   path("ver-compra/<solicitud>/",views.ver_compra,name="ver_compra"),
   path("recepcion-bodega/",views.recepcion_bodega,name="recepcion_bodega"),
   path("recepcion-registro/<solicitud>/",views.recepcion_registro,name="recepcion_registro"),
   path("ver-recepcion-registro/<solicitud>/",views.ver_recepcion,name="ver_recepcion"),
   path("modificar-recepcion-registro/<id>/",views.modificar_recepcion,name="modificar_recepcion"),
   path("ver-requisicion/<solicitud>/",views.requisiciones,name="requisiciones"),
   path("grafico/<villa>/",views.view_insumos,name="grafico_villa"),
   
  
    
]