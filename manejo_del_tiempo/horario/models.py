from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User


class Event(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.IntegerField(choices = [(i,i) for i in range(1,11)])
    name = models.CharField(max_length=30)
    description = models.CharField(max_length = 80)
    fixed = models.BooleanField()
    constraints = models.JSONField(default = dict)
    array_position1 = models.IntegerField(MaxValueValidator(7))
    array_position2 = models.IntegerField(MaxValueValidator(24))




class Schedule(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=60)








