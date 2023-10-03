from django.db import models
from datetime import date 
import socket
class Direccion(models.Model):
    calle_text = models.CharField(max_length=256)
    colonia_text = models.CharField(max_length=256)
    ciudad_text = models.CharField(max_length=256)
    estado_text = models.CharField(max_length=256)
    pais_text = models.CharField(max_length=256)
    codigo_text = models.CharField(max_length=5)
    numero_externo_number = models.IntegerField()
    @property
    def direccion_completa(self):
        return 'Calle: ' + self.calle_text.title() + ' #' + str(self.numero_externo_number) + ' Colonia: ' + self.colonia_text.title() + ' Municipio: ' + self.ciudad_text.title() + ' Estado: '+ self.estado_text.title() + ' Pais: ' + self.pais_text.title() + ' '
    

class Hoteles(models.Model):
    name_text = models.CharField(max_length=128)
    numero_habitaciones_numeber = models.IntegerField()
    telefono_text = models.CharField(max_length=10)
    direccion_fk = models.ForeignKey(Direccion,on_delete=models.CASCADE)

class Habitaciones(models.Model):
    codigo_hotel_fk = models.ForeignKey(Hoteles,on_delete=models.CASCADE)
    capacidad_personas = models.IntegerField()
    src = models.ImageField(null=True,upload_to='imagenes/habitaciones/')
    alt = models.CharField(max_length=128,default='Imagen')
    title_text = models.CharField(max_length=128, default='titulo')
    precio_hora_number = models.PositiveIntegerField()

class Generente(models.Model):
    name_text = models.CharField(max_length=128)
    last_name_text = models.CharField(max_length=64)
    middle_name_text = models.CharField(max_length=64)
    direccion_fk = models.ForeignKey(Direccion,on_delete=models.CASCADE)
    RFC_text = models.CharField(max_length=15,primary_key=True)
    codigo_hotel_fk = models.ForeignKey(Hoteles,on_delete=models.CASCADE)

class Usuarios(models.Model):
    acessos = [
        ("C", "Cliente"),
        ("A", "Administrador"),
    ] 
    src = models.ImageField(null=True, upload_to='imagenes/avaters/')
    alt = models.CharField(max_length=128,default='Imagen')
    username_text = models.CharField(max_length=32)
    email_text = models.CharField(max_length=128)
    password_text = models.CharField(max_length=64)
    nivel_acceso = models.CharField(max_length=1,default="C",choices=acessos)

class Imagenes(models.Model):
    path = models.CharField(max_length=512)
    alt = models.CharField(max_length=256)
    @property
    def src(self):
        return socket.gethostname()+self.path

class Clientes(models.Model):
    user_fk = models.ForeignKey(Usuarios,null=True,on_delete=models.CASCADE)
    name_text = models.CharField(max_length=64)
    last_name_text = models.CharField(max_length=64, null=True)
    fecha_nacimiento = models.DateField()
    middle_name_text = models.CharField(max_length=64,null=True)
    telefono_text = models.CharField(max_length=10,null=True)
    direccion_fk = models.ForeignKey(Direccion,on_delete=models.CASCADE)
    @property
    def formatdate(self):
        return self.fecha_nacimiento.strftime('%Y-%m-%d')
    @property
    def full_name(self):
        return f"{self.name_text} {self.last_name_text} {self.middle_name_text}"
    @property
    def edad(self):
        return (self.fecha_nacimiento - date.today()).days / 365.25

class cliente_habitacion(models.Model):
    persona_id_fk = models.ForeignKey(Clientes,on_delete=models.CASCADE)
    habitacion_id_fk = models.ForeignKey(Habitaciones,on_delete=models.CASCADE)
    imagen_id_fk = models.ForeignKey(Imagenes,on_delete=models.CASCADE)
    title_text = models.CharField(max_length=128)
    description_text = models.TextField(max_length=256)
    fecha_llegada_date = models.DateTimeField()
    fecha_salida_date = models.DateTimeField()