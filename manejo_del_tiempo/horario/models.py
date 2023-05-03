from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.IntegerField(choices = [(i,i) for i in range(1,11)])
    name = models.CharField(max_length=30)
    description = models.CharField(max_length = 80)
    fixed = models.BooleanField()
    constraints = models.JSONField(default = dict)




class Schedule(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    #ordered_schedule = [[]] Averiguar como almacenar este tipo de dato en sqlite








