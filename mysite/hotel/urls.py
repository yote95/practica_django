from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register',views.register_user, name='register'),
    path('login',views.login, name='login'),
    path('Detalle/<int:id>', views.detalle_habitacion, name='detalle_habitacion'),
]