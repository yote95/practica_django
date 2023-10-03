from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from const import method
def index(request):
    return render(request,'hotel/welcome.html',{'lista_habitaciones':models.Habitaciones.objects.all()})

def login(request):
    if request.method == method.post:   
        if models.Usuarios.objects.exists():
            user = models.objects.get(email=request.POST.get('email'),password=request.POST.get('password'))
            return HttpResponseRedirect('/hotel/',user=user)
        else:
            return HttpResponseRedirect('/hotel/login',error_message="Usuario o Contraseña Incorrectos")
    elif request.method == method.get:
        return render(request,'hotel/login.html')

def register_user(request):
    if request.method == method.post:
        user = models.Usuarios.objects.create(
            username_text=request.POST.get('username'),
            email_text=request.POST.get('email'),
            password_text=request.POST.get('password')
            )
        return HttpResponseRedirect('/hotel/',user=user)
    elif request.method == method.get:
        return render(request,'hotel/registro_usuario.html')


def detalle_habitacion(request, id_habitacion):
    habitacion = models.Habitaciones.objects.get(id=habitacion)
    hotel = models.Hoteles.objects.get(id=habitacion.codigo_hotel_fk)
    direccion = models.Direccion.objects.get(id=hotel.dirreccion_fk)
    if(request.method == method.put or request.method == method.path):
         return render(request, '/hotel/detalle_habitacion.html')
    elif(request.method == method.get):    
        return render(request,'/hotel/detalle_habitacion.html')
    elif(request.method == method.delete):
        models.Habitaciones.objects.get(id=id_habitacion).delete()
        return render(request,'/hotel/')