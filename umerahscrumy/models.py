from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class GoalStatus(models.Model):
    status_name = models.CharField(max_length = 120)
    

class ScrumyGoals(models.Model):
    goal_name = models.CharField(max_length= 120)
    goal_id = models.IntegerField()
    created_by = models.CharField(max_length = 120)
    moved_by = models.CharField(max_length = 120)
    owner = models.CharField(max_length = 120)
    goal_status = models.ForeignKey(GoalStatus, on_delete = models.PROTECT)
    user = models.ForeignKey(User, related_name= 'maps', on_delete = models.CASCADE)
  



class ScrumyHistory(models.Model):
    moved_by = models.CharField(max_length = 120) 
    created_by = models.CharField(max_length = 120)
    moved_from = models.CharField(max_length = 120)
    moved_to = models.CharField(max_length = 120)
    time_of_action = models.TimeField()
    goal = models.ForeignKey(ScrumyGoals, on_delete = models.CASCADE)

  



