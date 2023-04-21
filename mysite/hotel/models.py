from django.db import models
from datetime import date 
class Direccion(models.Model):
    calle_text = models.CharField(max_length=256)
    colonia_text = models.CharField(max_length=256)
    ciudad_text = models.CharField(max_length=256)
    estado_text = models.CharField(max_length=256)
    pais_text = models.CharField(max_length=256)
    codigo_text = models.CharField(max_length=5)
    numero_externo_number = models.IntegerField()

class Clientes(models.Model):
    name_text = models.CharField(max_length=64)
    last_name_text = models.CharField(max_length=64)
    fecha_nacimiento = models.DateField()
    middle_name_text = models.CharField(max_length=64)
    telefono_text = models.CharField(max_length=10)
    dirreccion_fk = models.ForeignKey(Direccion)
    @property
    def full_name(self):
        return f"{self.name_text} {self.last_name_text} {self.middle_name_text}"
    @property
    def edad(self):
        return (self.fecha_nacimiento - date.today()).days / 365

class Hoteles(models.Model):
    name_text = models.CharField(max_length=128)
    numero_habitaciones_numeber = models.IntegerField()
    telefono_text = models.CharField(max_length=10)
    dirreccion_fk = models.ForeignKey(Direccion)

class Habitaciones(models.Model):
    codigo_hotel_fk = models.ForeignKey(Hoteles)
    capacidad_personas = models.IntegerField()
    precio_hora_number = models.PositiveIntegerField()

class Generente(models.Model):
    name_text = models.CharField(max_length=128)
    last_name_text = models.CharField(max_length=64)
    middle_name_text = models.CharField(max_length=64)
    direccion_fk = models.ForeignKey(Direccion)
    RFC_text = models.CharField(min_length=15,max_length=15,primary_key=True)
    codigo_hotel_fk = models.ForeignKey(Hoteles)

class Usuarios(models.Model):
    acessos = [
        ("C", "Cliente"),
        ("A", "Administrador"),
    ]
    username_text = models.CharField(max_length=32)
    email_text = models.CharField(max_length=128)
    password_text = models.CharField(max_length=64)
    nivel_acceso = models.CharField(max_length=1,default="C",choices=acessos)

class cliente_habitacion(models.Model):
    persona_id_fk = models.ForeignKey(Clientes)
    habitacion_id_fk = models.ForeignKey(Habitaciones)
    fecha_llegada_date = models.DateTimeField()
    fecha_salida_date = models.DateTimeField()