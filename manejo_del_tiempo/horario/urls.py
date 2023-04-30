from django.urls import path
from . import views

urlpatterns = [
		path('',views.horario, name = 'horario'),
        path('user_login',views.user_login, name = 'user_login'),
        path('user_logout',views.user_logout, name = 'user_logout'),
        path('user_register',views.user_register, name = 'user_register'),
        path('suenio',views.suenio, name = 'suenio'),
        path('actividades_fijas',views.actividades_fijas, name = 'actividades_fijas'),
        path('actividades_fijas/crear_actividades_fijas',views.crear_actividades_fijas, name = 'crear_actividades_fijas'),
        path('actividades_fijas/eliminar_actividades_fijas',views.eliminar_actividades_fijas, name = 'eliminar_actividades_fijas'),
        path('actividades_no_fijas',views.actividades_no_fijas, name = 'actividades_no_fijas'),
        path('actividades_no_fijas/crear_actividades_no_fijas',views.crear_actividades_no_fijas, name = 'crear_actividades_no_fijas'),
        path('actividades_no_fijas/eliminar_actividades_no_fijas',views.eliminar_actividades_no_fijas, name = 'eliminar_actividades_no_fijas'),
]