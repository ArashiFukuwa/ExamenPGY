from os import name
from django.db import router
from django.urls import path,include
from .views import * 
from rest_framework import routers

router = routers.DefaultRouter()
router.register('productos', ProductoViewSet)

urlpatterns = [
    path('',index , name="index" ),
    path('productos/', productos, name="productos" ),
    path('contacto/', contacto, name="contacto" ),
    path('agregar-producto/', agregar_producto, name="agregar_producto" ),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto" ),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto" ),
    path('quiensomos/',quiensomos , name="quiensomos"),
    path('horario/',horario,name="horario"),
    path('registro-usuario/',registro_usuario, name="registro_usuario"),
    path('suscripcion/',suscriptor,name="suscripcion"),
    path('api/',include(router.urls))
    



]

