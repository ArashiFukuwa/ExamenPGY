from rest_framework import serializers
from .models import Producto,TipoProducto
from django.forms import ValidationError

class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model=TipoProducto
        fields='__all__'

class ProductoSerializer(serializers.ModelSerializer):
    tipo = TipoProductoSerializer(read_only=True)
    tipo_producto=serializers.PrimaryKeyRelatedField(queryset=TipoProducto.objects.all(),source="tipo")
    class Meta:
        model = Producto
        fields = '__all__'

    def validate_nombre(self,value):
        aux = Producto.objects.filter(nombre__iexact=value).exists()
         
        if aux:
            raise ValidationError("Este Producto ya existe.")
        return value


    def validate_precio(self,value):
         
        if value<9000:
            raise ValidationError("El precio no puede ser menor a 9000.")
        return value