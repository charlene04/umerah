from django.shortcuts import render
from . import models

# Create your views here.

from django.http import HttpResponse  


def index(request):
    goal = models.ScrumyGoals.objects.get(goal_name = 'Learn Django')
    return HttpResponse(goal.goal_name) 