from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from const import method
#from rest_framework.decorators import api_view
from .forms import users

class views(): 
    def __init__(self):
        self.user = None
    def index(self,request):
        habitaciones = models.Habitaciones.objects.all()
        return render(request,'hotel/welcome.html',{'user':self.user, 'lista_habitaciones':habitaciones})
    #@api_view(['GET','POST','PUT','DELETE'])
    def users(self,request, id= 0):
        if request.method == method.get:
            if models.Usuarios.objects.filter(pk=id).exists():
                self.user = models.Usuarios.objects.get(pk=id)
                cliente = models.Clientes.objects.filter(user_fk=self.user.id).first()
                return render(request,'hotel/editar_usuario.html',{'user':self.user, 'cliente':cliente})
            else:
                self.user = None
                return HttpResponseRedirect('/')
        elif request.method == method.post:
            user = models.Usuarios.objects.get(pk=id)
            cliente = models.Clientes.objects.filter(user_fk=id).first()
            if request.POST.get('_method') == method.put or request.POST.get('_method') == method.path:
                form = users(request.POST, request.FILES)
                if len(request.FILES) > 0:
                    user.src = request.FILES['foto_perfil']
                if request.POST.get('pasado_contrasena') == user.password_text:
                    user.password_text = request.POST.get('contrasena')
                user.save()
                self.user = user
                cliente.fecha_nacimiento = request.POST.get('fecha_nacimiento')
                cliente.name_text = request.POST.get('nombre')
                cliente.last_name_text = request.POST.get('apellido_paterno')
                cliente.middle_name_text= request.POST.get('apellido_materno')
                cliente.telefono_text = request.POST.get('telefono')
                cliente.direccion_fk.calle_text=request.POST.get('calle')
                cliente.direccion_fk.colonia_text=request.POST.get('colonia')
                cliente.direccion_fk.ciudad_text= request.POST.get('municipio')
                cliente.direccion_fk.estado_text=request.POST.get('estado')
                cliente.direccion_fk.pais_text = request.POST.get('pais')
                cliente.direccion_fk.codigo_text = request.POST.get('codigo_postal')
                cliente.direccion_fk.numero_externo_number = int(request.POST.get('no_externo'))
                cliente.direccion_fk.save()
                cliente.save()
                return HttpResponseRedirect('/')
            elif request.POST.get('_method') == method.delete:
                direccion = models.Direccion.objects.get(pk=cliente.direccion_fk.id)
                cliente.delete()
                direccion.delete()
                user.delete()
                return HttpResponseRedirect('/')
            else:
                self.user = None
                return HttpResponseRedirect('/')

    def login(self,request):
        if request.method == method.post:   
            if models.Usuarios.objects.filter(
                    username_text=request.POST.get('username'),
                    password_text=request.POST.get('password')).exists():
                self.user = models.Usuarios.objects.filter(
                    username_text=request.POST.get('username'),
                    password_text=request.POST.get('password')).first()
                habitaciones = models.Habitaciones.objects.all()
                return HttpResponseRedirect('/',{'user':self.user, 'lista_habitaciones':habitaciones})
            else:
                return render(request,'hotel/login.html',{'user':self.user,'error_message':"Usuario o Contraseña Incorrectos"})
        elif request.method == method.get:
            return render(request,'hotel/login.html',{'user':self.user,'error_message':None})

    def register_user(self,request):
        if request.method == method.post:
            self.user = models.Usuarios.objects.create(
                username_text=request.POST.get('usuario'),
                email_text=request.POST.get('correo'),
                password_text=request.POST.get('contrasena')
            )
            if len(request.FILES) > 0:
                self.user.src = request.FILES['foto_perfil']
                self.user.save()
            direccion = models.Direccion.objects.create(
                calle_text=request.POST.get('calle'),
                colonia_text=request.POST.get('colonia'),
                ciudad_text= request.POST.get('municipio'),
                estado_text=request.POST.get('estado'),
                pais_text = request.POST.get('pais'),
                codigo_text = request.POST.get('codigo_postal'),
                numero_externo_number = request.POST.get('no_externo')
            )
            #genero = models.Clientes.generos['M']
            #if request.POST.get('genero') == 'F':
            #    genero = models.Clientes.generos('F')

            cliente = models.Clientes.objects.create(
                user_fk=self.user,
                name_text = request.POST.get('nombre'),
                last_name_text = request.POST.get('apellido_paterno'),
                fecha_nacimiento = request.POST.get('fecha_nacimiento'),
                middle_name_text= request.POST.get('apellido_materno'),
                telefono_text = request.POST.get('telefono'),
                direccion_fk =direccion
            )
            return HttpResponseRedirect('/')
        elif request.method == method.get:
            return render(request,'hotel/registro_usuario.html',{'user':self.user})


    def detalle_habitacion(self,request, id_habitacion):
        habitacion = models.Habitaciones.objects.get(id=habitacion)
        hotel = models.Hoteles.objects.get(id=habitacion.codigo_hotel_fk)
        direccion = models.Direccion.objects.get(id=hotel.dirreccion_fk)
        if(request.method == method.put or request.method == method.path):
             return render(request, '/hotel/detalle_habitacion.html')
        elif(request.method == method.get):    
            return render(request,'/hotel/detalle_habitacion.html')
        elif(request.method == method.delete):
            models.Habitaciones.objects.get(id=id_habitacion).delete()
            return HttpResponseRedirect('/',{'user':self.user})

    def habitacion(self,request, id =1):
        if request.method == method.post:
            return HttpResponseRedirect('/',{'user':self.user})
        elif request.method == method.get:
            habitacion = models.Habitaciones.objects.get(pk=id)
            return render(request, "hotel/detalle_habitacion.html", {'user':self.user,'habitacion':habitacion, 'hotel':habitacion.codigo_hotel_fk})
    
    def admin_web(self, request):
        hoteles = models.Hoteles.objects.all()
        habitaciones = models.Habitaciones.objects.all()
        return render(request, "hotel/admin_web.html", {'user':self.user, 'hoteles':hoteles, 'habitaciones':habitaciones})

    def registrar_hoteles(self, request):
        if request.method == method.post:
            direccion = models.Direccion.objects.create(
                calle_text=request.POST.get('calle'),
                colonia_text=request.POST.get('colonia'),
                ciudad_text= request.POST.get('municipio'),
                estado_text=request.POST.get('estado'),
                pais_text = request.POST.get('pais'),
                codigo_text = request.POST.get('codigo_postal'),
                numero_externo_number = request.POST.get('no_externo')
            )
            models.Hoteles.objects.create(
                name_text=request.POST.get('name'),
                numero_habitaciones_numeber= request.POST.get('numero_habitaciones'),
                telefono_text=request.POST.get('telefono'),
                direccion_fk=direccion
            )
            return HttpResponseRedirect('/adminhotel')
        else:
            return render(request, "hotel/registrar_hotel.html", {'user':self.user})

    def gestionar_hoteles(self, request, id):
        hotel = models.Hoteles.objects.get(pk=id)
        if request.method == method.post:
            if request.POST.get('_method') == method.put:
                hotel.name_text=request.POST.get('name')
                hotel.numero_habitaciones_numeber= request.POST.get('numero_habitaciones')
                hotel.telefono_text=request.POST.get('telefono')
                hotel.direccion_fk.calle_text=request.POST.get('calle')
                hotel.direccion_fk.colonia_text=request.POST.get('colonia')
                hotel.direccion_fk.ciudad_text= request.POST.get('municipio')
                hotel.direccion_fk.estado_text=request.POST.get('estado')
                hotel.direccion_fk.pais_text = request.POST.get('pais')
                hotel.direccion_fk.codigo_text = request.POST.get('codigo_postal')
                hotel.direccion_fk.numero_externo_number = request.POST.get('no_externo')
                hotel.direccion_fk.save()
                hotel.save()
                return HttpResponseRedirect('/adminhotel')
            elif request.POST.get('_method') == method.delete:
                direccion = models.Direccion.objects.get(pk=hotel.direccion_fk.id)
                hotel.delete()
                direccion.delete()
                return HttpResponseRedirect('/adminhotel')
            else:
                return HttpResponseRedirect('/adminhotel')
        else:
            return render(request, "hotel/editar_hotel.html", {'hotel':hotel})

    def registar_habitacion(self, request):
        hoteles = models.Hoteles.objects.all()
        
        if request.method == method.post:
            habitacion = models.Habitaciones.objects.create(
                capacidad_personas=request.POST.get('capacidad_personas'),
                title_text= request.POST.get('title'),
                precio_hora_number=request.POST.get('precio'),
                codigo_hotel_fk=hoteles.get(pk=request.POST.get('hotel'))
            )
            if len(request.FILES) > 0:
                habitacion.src = request.FILES['photo']
                habitacion.save()
            return HttpResponseRedirect('/adminhotel')
        else:
            return render(request, "hotel/registrar_habitacion.html", {'hoteles':hoteles})
        
    def gestionar_habitacion(self, request, id):
        hoteles = models.Hoteles.objects.all()
        habitacion = models.Habitaciones.objects.get(pk=id)
        if request.method == method.post:
            if request.POST.get('_method') == method.put:
                habitacion.capacidad_personas=request.POST.get('capacidad_personas')
                habitacion.title_text= request.POST.get('title')
                habitacion.precio_hora_number=request.POST.get('precio')
                habitacion.codigo_hotel_fk=hoteles.get(pk=request.POST.get('hotel'))
                if len(request.FILES) > 0:
                    habitacion.src = request.FILES['photo']
                habitacion.save()
                return HttpResponseRedirect('/adminhotel')
            elif request.POST.get('_method') == method.delete:
                habitacion.delete()
                return HttpResponseRedirect('/adminhotel')
            else:
                return HttpResponseRedirect('/adminhotel')
        else:
            return render(request, "hotel/editar_habitacion.html", {'hoteles':hoteles, 'habitacion':habitacion,'user':self.user})
        
view = views()