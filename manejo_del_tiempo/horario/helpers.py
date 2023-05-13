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

