from django.db import models

# Create your models here.
class TipoProducto(models.Model):
    tipo = models.CharField(max_length=40)

    def __str__(self):
        return self.tipo

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()
    oferta = models.IntegerField( )
    descripcion = models.CharField(max_length=40)
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    fecha = models.DateField()
    imagen = models.ImageField(null=True,blank=True)


    def __str__(self):
        return self.nombre

opcion_pago = [
    [0,"CREDITO"],
    [1,"DEBITO"],
    [2,"TARJETA DIGITAL"],
    [3,"PAYPAL"],
]

opcion_aviso = [
    [0,"SI"],
    [1,"NO"],
]

class suscriptor(models.Model):
    nombre = models.CharField(max_length=40)
    correo = models.EmailField()
    tipo_pago=models.IntegerField(choices=opcion_pago)
    aviso=models.IntegerField(choices=opcion_aviso)
    monto_donation=models.IntegerField()

    def __str__(self):
        return self.nombre





# python manage.py makemigrations -- CREA EL ARCHIVO DE MIGRACIÓN PARA LA BD 
# python manage.py migrate -- ENVIA EL ARCHIVO A LA BD 
# python manage.py createsuperuser -- CREA EL ADMIN DE LA WEB
# pip install pillow -- NOS PERMITE TRABAJAR CON LAS IMAGENES DE DJANGO