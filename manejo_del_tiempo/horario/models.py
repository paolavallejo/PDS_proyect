from django.db import models
from django.contrib.auth.models import User


#choices de dias de semana:
DIA_LUNES = 'Lunes'
DIA_MARTES = 'Martes'
DIA_MIERCOLES = 'Miércoles'
DIA_JUEVES = 'Jueves'
DIA_VIERNES = 'Viernes'
DIA_SABADO = 'Sábado'
DIA_DOMINGO = 'Domingo'
DIA_CHOICES = [
    (DIA_LUNES, 'Lunes'),
    (DIA_MARTES, 'Martes'),
    (DIA_MIERCOLES, 'Miércoles'),
    (DIA_JUEVES, 'Jueves'),
    (DIA_VIERNES, 'Viernes'),
    (DIA_SABADO, 'Sábado'),
    (DIA_DOMINGO, 'Domingo'),
    ]




class Horario_sueno(models.Model):
    usuario_id = models.ForeignKey(User,on_delete=models.CASCADE)
    horas_semanales = models.TimeField()
    hora_maxima_levantar = models.TimeField()
    hora_minima_acostar = models.TimeField()
    longitud_maxima_sueno = models.TimeField()
    longitud_minima_sueno = models.TimeField()




class Actividad_no_fija(models.Model):
    usuario_id = models.ForeignKey(User,on_delete=models.CASCADE)
    nombre_actividad = models.CharField(max_length=60)
    descripcion_actividad = models.CharField(max_length=400)




#Todas las actividades no fijas y horarios de sueno luego pasarán a ser actividades fijas.
class Actividad_fija(models.Model):
    usuario_id = models.ForeignKey(User,on_delete=models.CASCADE)
    nombre_actividad = models.CharField(max_length=60)
    descripcion_actividad = models.CharField(max_length=400)
    dia_realizacion = models.CharField(max_length=10,choices=DIA_CHOICES)
    hora_realizacion = models.TimeField()
    demora_actividad = models.TimeField()
    tiempo_transporte = models.TimeField()
    tipo_actividad = models.CharField(max_length=40,choices=[('no_fija','no_fija'),('fija','fija'),('sueno','sueno')])









