from .models import Position

def registrar_posiciones(actividades):
    schedule = [[ None for period in range(24)] for day in range(7)]

    for actividad_fija in actividades:
        posiciones = Position.objects.filter(event_id = actividad_fija.pk)
        for pos in posiciones:
            dia = pos.day
            hora = pos.hour

            schedule[dia][hora] = actividad_fija
    
    return schedule



# Go over each element by priority
# Check if the element´s minimum time can fit on the time alloted
# If not, take next element
# If it fits, test the next series until it fails

def generate_schedule(schedule, adaptable_events):
    # TO DO
    repeats = 0
    adaptable_events_locations = []
    adaptable_events = list(adaptable_events)
    # Go over each hour in schedule
    for day in range(len(schedule)):
        repeats = 0
        for hour in range(len(schedule[day])):
            adaptable_events.sort(key = lambda event: event.priority, reverse = True)

            event_idx = 0

            # Go over each element by priority
            while schedule[day][hour] == None and event_idx < len(adaptable_events):
                # Check if it is in valid range, or if it already spent
                if hour in range(adaptable_events[event_idx].constraints["earliest_hour"], adaptable_events[event_idx].constraints["latest_hour"]+1) and adaptable_events[event_idx].constraints["time_goal_counter"] != 0:
                    
                    # Check maximum time
                    if  hour > 0:
                        if adaptable_events[event_idx] == schedule[day][hour - 1]:
                            repeats += 1

                    if repeats != adaptable_events[event_idx].constraints["max_time"]:
                        adaptable_events_locations.append((adaptable_events[event_idx], (day, hour)))
                        schedule[day][hour] = adaptable_events[event_idx]
                        adaptable_events[event_idx].constraints["time_goal_counter"] = adaptable_events[event_idx].constraints["time_goal_counter"] - 1
                        

                event_idx += 1
    return adaptable_events_locations




def eliminar_posiciones_actividades(actividades):

    for actividad in actividades:
            posiciones = Position.objects.filter(event_id = actividad)
            posiciones.delete()




# Insertar Sueño
def insertar_suenio(schedule, horario_suenio):
    suenio_locations = []
    if len(horario_suenio) == 1:
        horario_suenio = horario_suenio[0]
        constraints = horario_suenio.constraints
        duracion_max = round((constraints["time_goal"])/7,0)
        

        for day in range(len(schedule)):
            repite = 0
            for hour in range(len(schedule[day])):
                if repite < duracion_max:
                    if schedule[day][hour] == None and hour < constraints["max_levantarse"] and constraints["time_goal_counter"] != 0:

                        schedule[day][hour] = horario_suenio
                        suenio_locations.append((horario_suenio, (day, hour)))
                        constraints["time_goal_counter"] = constraints["time_goal_counter"] - 1
                        repite +=1

                    if schedule[day][23-hour] == None and (23-hour) >= constraints["max_acostarse"] and constraints["time_goal_counter"] != 0:

                        schedule[day][23-hour] = horario_suenio
                        suenio_locations.append((horario_suenio, (day, 23-hour)))
                        constraints["time_goal_counter"] = constraints["time_goal_counter"] - 1
                        repite +=1

        return suenio_locations
    else:
        return suenio_locations

