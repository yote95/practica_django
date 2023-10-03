from django.contrib import admin
from .models import Usuarios, Hoteles,Habitaciones,Generente
admin.site.register(Usuarios)
admin.site.register(Generente)
admin.site.register(Habitaciones)
admin.site.register(Hoteles)
