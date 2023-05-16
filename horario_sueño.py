# Insertar Sueño
def insertar_sueño(schedule, horario_suenio):

    constraints = horario_suenio.constraints
    duracion_max = round(constraints["time_goal"]/7, 0)

    for day in range(len(schedule)):
        repite = 0
        for hour in range(len(schedule[day])):
            if repite < duracion_max:
                if schedule[day][hour] == None and hour < constraints["max_levantarse"] and constraints["time_goal_counter"] != 0:

                    schedule[day][hour] = horario_suenio
                    constraints["time_goal_counter"] = constraints["time_goal_counter"] - 1
                    repite +=1

                if schedule[day][23-hour] == None and (23-hour) >= constraints["max_acostarse"] and constraints["time_goal_counter"] != 0:

                    schedule[day][23-hour] = horario_suenio
                    constraints["time_goal_counter"] = constraints["time_goal_counter"] - 1
                    repite +=1

    return schedule
