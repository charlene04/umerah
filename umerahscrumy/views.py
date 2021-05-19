from django.shortcuts import render
from django.contrib.auth.models import User
from . import models
import random
# Create your views here.

from django.http import HttpResponse  


def index(request):
    goal = models.ScrumyGoals.objects.get(goal_name = 'Learn Django')
    return HttpResponse(goal.goal_name) 



def move_goal(request, goal_id):
    goal = models.ScrumyGoals.objects.get(goal_id = goal_id)
    return HttpResponse(goal.goal_name) 
idList = []

def add_goal(request):
    ID = []
    i = 0
    while i < len(idList) + 1:
        rnd = random.randint(1000 , 9999)
        if rnd in idList:
            continue
        ID.append(rnd)
        i = i+ 1
    requiredID = ID[0]
    idList.append(requiredID)
    
    models.ScrumyGoals.objects.create(goal_name = "Keep Learning Django", 
                                        goal_id = requiredID,
                                        created_by = "louis", 
                                        moved_by = "louis",
                                        owner = "louis",
                                        goal_status =  models.GoalStatus.objects.get   (status_name = "Weekly Goal"), 
                                        user = User.objects.get(username = "louis"))
                                        
    return HttpResponse("ok") 
   
def home(request):
    goals = models.ScrumyGoal.objects.filter(goal_name = "Keep Learning Django")
    output = ', '.join([eachgoal.goal_name for eachgoal in goals]) 
    
    return HttpResponse(output) 