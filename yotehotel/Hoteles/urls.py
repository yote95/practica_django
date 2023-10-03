from django.urls import path
from .views import view

urlpatterns = [
    path('', view.index),
    path('login', view.login, name="login"),
    path('register', view.register_user, name="register"),
    path('habitacion/<int:id>/', view.habitacion, name="habitacion"),
    path('user/<int:id>/', view.users, name="user"),
    path('adminhotel', view.admin_web, name="admin"),
    path('adminhotel/hotel', view.registrar_hoteles, name="hotel"),
    path('adminhotel/hotel/<int:id>/', view.gestionar_hoteles, name="editarhotel"),
    path('adminhotel/habitacion', view.registar_habitacion, name="registarhabitacion"),
    path('adminhotel/habitacion/<int:id>', view.gestionar_habitacion, name="editarhabitacion"),
]