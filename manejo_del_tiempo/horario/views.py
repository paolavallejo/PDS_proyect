from django.shortcuts import render
from django.http import HttpResponse


#Ruta principal:
def horario(request):
    return HttpResponse("Estás en la página principal")


#Registro de usuario, login y logout:
def user_login(request):
    return HttpResponse("Estás en el user login")




def user_logout(request):
    return HttpResponse("Estás en el user logout")




def user_register(request):
    return HttpResponse("Estás en el user register")



#Adquirir datos de sueño:
def suenio(request):
    return HttpResponse("Estás en la pagina de sueño")



#Adquirir y mostrar actividades fijas:
def actividades_fijas(request):
    return HttpResponse("Estás en la pagina de actividades fijas")



def crear_actividades_fijas(request):
    return HttpResponse("Estás en la pagina de crear actividades fijas")



def eliminar_actividades_fijas(request):
    return HttpResponse("Estás en la pagina de eliminar actividades fijas")



#Adquirir y mostrar actividades no fijas
def actividades_no_fijas(request):
    return HttpResponse("Estás en la pagina de actividades no fijas")




def crear_actividades_no_fijas(request):
    return HttpResponse("Estás en la pagina de crear actividades no fijas")



def eliminar_actividades_no_fijas(request):
    return HttpResponse("Estás en la pagina de eliminar actividades no fijas")




#Vista que crea el horario final y lo muestra en pantalla:
def horario_final(request):
    return HttpResponse("Estás en la pagina que despliega el horario final")

