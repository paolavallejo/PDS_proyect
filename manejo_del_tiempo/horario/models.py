from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User


class Event(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.IntegerField(choices = [(i,i) for i in range(1,11)])
    name = models.CharField(max_length=30)
    fixed = models.BooleanField()
    constraints = models.JSONField(default = dict)

    #constraints: (time_goal_counter),horas_por_semana(time_goal), más temprano para hacer la actividad(earliest_hour),(latest_hour),max_time  



class Position(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    day = models.IntegerField(MaxValueValidator(7))
    hour = models.IntegerField(MaxValueValidator(24))








