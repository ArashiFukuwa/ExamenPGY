from typing import ValuesView
from django import forms
from django.db import models
from django.forms import ModelForm, fields, widgets
from django.http.request import validate_host
from .models import Producto, suscriptor
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import TamañoMaximoValidator

class ProductoForm(ModelForm):

    nombre= forms.CharField(min_length=5,max_length=50)
    precio= forms.IntegerField(min_value=9000)
    oferta= forms.IntegerField(min_value=1000)
    imagen= forms.ImageField(validators=[TamañoMaximoValidator(1)],required=False)

    def clean_nombre(self):
        nom = self.cleaned_data["nombre"]
        aux = Producto.objects.filter(nombre__iexact=nom).exists()

        if aux:
            raise ValidationError("Este juego ya existe.")
        return nom

    class Meta:             
        model = Producto
        fields = ['nombre','precio','oferta','descripcion','tipo','fecha','imagen']

        widgets = {
            'fecha' : forms.SelectDateWidget(years=range(2018,2022))
        }

class UsuarioCreationForm(UserCreationForm):

    class Meta:
        model = User
        # fields = 'all'
        fields = ['username','first_name','last_name','email','password1','password2']

class suscriptorForm(ModelForm):
    monto_donation = forms.IntegerField(min_value=2000)

    class Meta:
        model = suscriptor
        fields = ['nombre','correo','tipo_pago','aviso','monto_donation']