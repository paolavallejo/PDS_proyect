from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages #para mandar mensajes de error
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Event, Position


#Ruta principal:
def horario(request):
    return render(request,"horario.html")



#Registro de usuario, login y logout:
def user_login(request):
    
    if request.method == "POST":
        username = request.POST.get("usuario").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request,"¡Usuario no existe!")
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect(reverse('horario'))
        elif user == None:
            messages.error(request,"¡Clave erronea!")

    return render(request,"user_login.html")


@login_required(login_url = "user_login")
def user_logout(request):
    logout(request)
    return redirect(reverse('user_login'))




def user_register(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect(reverse("horario"))
        
    return render(request,'user_register.html',{'UserCreationForm':UserCreationForm})
        
    



#Adquirir datos de sueño:
@login_required(login_url = "user_login")
def suenio(request):
    if request.method == "POST":
        #Atributos:
        #
        #
        #

        #constraints: 
        # time_goal: horas semanales sueño
        # time_goal_counter: horas semanales sueño
        # max_levantarse: hora máxima levantar
        # max_acostarse: hora máxima acostar 
        # max_time: máximo tiempo de dormir seguido
        
        name = "horario_suenio"
        pass
        

    elif request.method == "GET":
        return render(request,"suenio.html")
    

@login_required(login_url = "user_login")
def eliminar_suenio(request,ruta_suenio):
    return HttpResponse("Estás en la pagina de eliminar horario de sueño")




#Adquirir y mostrar actividades fijas:
'''Atributos:
        User_id 
        priority = 10
        name
        Event_type = Actividad_no_fija
        

    Constraints:
        No maneja constraints'''
@login_required(login_url = "user_login")
def actividades_fijas(request):
    usuario = User.objects.get(pk=request.user.pk)
    if request.method == "POST":

        nombre = request.POST['name']
        prioridad = 10
        tipo_evento = "actividad_fija"

        nueva_actividad_fija = Event(user_id = usuario, priority = prioridad, name=nombre, event_type=tipo_evento)
        nueva_actividad_fija.save()

        #Crear registro de Position para cada posicion que ocupa el evento:

        dia_actividad = int(request.POST['dia_actividad'])
        hora_actividad = int(request.POST["hora_actividad"])-1
        duracion_actividad = int(request.POST["duracion_actividad"])
        hora_final = hora_actividad + duracion_actividad

        for hora in range(hora_actividad,hora_final,1):
            posicion_actividad_fija = Position(event_id = nueva_actividad_fija,user_id = usuario,day=dia_actividad,hour = hora)
            posicion_actividad_fija.save()
        return redirect(reverse("actividades_fijas"))

    
    elif request.method == "GET":
        actividades_fijas = Event.objects.filter(user_id = usuario)
        actividades_fijas =actividades_fijas.filter(event_type = "actividad_fija")
        return render(request,"actividades_fijas.html",{"actividades_fijas":actividades_fijas})



@login_required(login_url = "user_login")
def eliminar_actividades_fijas(request,ruta_actividad_fija):
    return HttpResponse("Estás en la pagina de eliminar actividades fijas")




#Adquirir y mostrar actividades no fijas
@login_required(login_url = "user_login")
def actividades_no_fijas(request):
    if request.method == "POST":
        #Atributos:
        #User_id -
        #priority -
        #Name -
        #Event_type = actividad_no_fija -

        #Constraints:
        # time_goal: horas semanales actividad 
        # time_goal_counter: horas semanales actividad 2
        # earliest_hour: hora más temprana
        # latest_hour: hora máxima realizar actividad  
        # max_time: máximo tiempo para realizar actividad 
        pass


    elif request.method == "GET":
        return render(request,"actividades_no_fijas.html")



@login_required(login_url = "user_login")
def eliminar_actividades_no_fijas(request,ruta_actividad_no_fija):
    return HttpResponse("Estás en la pagina de eliminar actividades no fijas")




#Vista que crea el horario final y lo muestra en pantalla:
@login_required(login_url = "user_login")
def horario_final(request):
    return render(request,"horario_final.html")

