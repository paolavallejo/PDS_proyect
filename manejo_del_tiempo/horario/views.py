from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages #para mandar mensajes de error
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


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
        pass


    elif request.method == "GET":
        return render(request,"suenio.html")
    



#Adquirir y mostrar actividades fijas:
@login_required(login_url = "user_login")
def actividades_fijas(request):
    return render(request,"actividades_fijas.html")



@login_required(login_url = "user_login")
def eliminar_actividades_fijas(request):
    return HttpResponse("Estás en la pagina de eliminar actividades fijas")



#Adquirir y mostrar actividades no fijas
@login_required(login_url = "user_login")
def actividades_no_fijas(request):
    return render(request,"actividades_no_fijas.html")



@login_required(login_url = "user_login")
def eliminar_actividades_no_fijas(request):
    return HttpResponse("Estás en la pagina de eliminar actividades no fijas")



#Vista que crea el horario final y lo muestra en pantalla:
@login_required(login_url = "user_login")
def horario_final(request):
    return render(request,"horario_final.html")

