from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages #para mandar mensajes de error
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Event, Position

# Jacobo me pidio que pusiera este comentario pa que se acordara
# Crear una matriz bidimensional basada en los datos fijos en bases de datos

def crear_matriz_horario():
    # Sacar eventos del usuario de base de datos
    actividades_fijas = Event.objects.filter(event_type="actividad_fija")
    actividades_fijas = actividades_fijas.objects.filter(usuario_id = request.user.pk)

    # Sacar posiciones de eventos de base de datos
    schedule = [[ None for period in range(24)] for day in range(7)]

    for actividad_fija in actividades_fijas:
        posiciones = Position.objects.filter(event_id = actividad_fija.pk)
        for pos in posiciones:
            dia = pos.dia
            hora = pos.hora

            schedule[dia][hora] = actividad_fija
    return schedule