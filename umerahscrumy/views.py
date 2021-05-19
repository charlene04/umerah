from django.shortcuts import render
from models import ScrumyGoals

# Create your views here.

from django.http import HttpResponse  


def index(request):
    goal = ScrumyGoals.objects.get(goal_name = 'Learn Django')
    return HttpResponse(goal.goal_name) 