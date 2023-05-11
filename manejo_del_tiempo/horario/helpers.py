from .models import Position

def registrar_posiciones(actividades_fijas):
    schedule = [[ None for period in range(24)] for day in range(7)]

    for actividad_fija in actividades_fijas:
        posiciones = Position.objects.filter(event_id = actividad_fija.pk)
        for pos in posiciones:
            dia = pos.day
            hora = pos.hour

            schedule[dia][hora] = actividad_fija
    
    return schedule