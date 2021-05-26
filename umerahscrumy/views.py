from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from . import form
from django.contrib.auth import login
from django.contrib.auth import authenticate
GroupDeveloper = Group.objects.get(name = 'Developer') 
GroupOwner = Group.objects.get(name = 'Owner')
GroupQualityAssurance = Group.objects.get(name = 'Quality Assurance')
GroupAdmin = Group.objects.get(name = 'Admin')
import random

#yes I will black 
from django.http import HttpResponse  


def index(request):
    if request.method == 'POST': 
        formView = form.SignupForm(request.POST) 
        if formView.is_valid():
            #post = form.save(commit=False)
            newUser = formView.save(commit = False)
            newUser.set_password(request.POST.get('password'))
            newUser.save()
            GroupDeveloper.user_set.add(newUser)
            return HttpResponse('YOUR ACCOUNT HAS BEEN CREATED SUCCESSFULLY')
    else: 
        formView = form.SignupForm()
        return render(request, 'umerahscrumy/index.html', {'form': formView})



def move_goal(request, goal_id):
    try:
        goal = models.ScrumyGoals.objects.get(goal_id = goal_id)
    except Exception as e: 
        return render(request, 'umerahscrumy/exception.html', {"error": "A record with that goal id does not exist"}) 
    else: 
        return HttpResponse(goal.goal_name) 
idList = []

def add_goal(request):
    if request.method == 'POST': 
        if request.user.groups.filter(name__in=[GroupAdmin]).exists():
            return render(request, 'umerahscrumy/exception.html', {'error': 'Sorry, your job is to move goals to and fro statuses.'})
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
    
        models.ScrumyGoals.objects.create(goal_name = request.POST.get('goal_name'), 
                                        goal_id = requiredID,
                                        created_by = request.user.username, 
                                        moved_by = request.user.username,
                                        owner = request.user.username,
                                        goal_status =  models.GoalStatus.objects.get(status_name = "Weekly Goal"), 
                                        user = User.objects.get(username = request.POST.get('user')))
        return redirect("umerahscrumy:home") 
    else:
        if request.user.groups.filter(name__in=[GroupDeveloper, GroupQualityAssurance, GroupOwner]).exists():
            return render(request, 'umerahscrumy/addgoal.html', {'users': User.objects.filter(username = request.user.username)})
        else:
            return render(request, 'umerahscrumy/addgoal.html', {'users': User.objects.all()})
   
def home(request):
    context = {'users': User.objects.all(), 
                'weeklyGoals': models.ScrumyGoals.objects.filter(goal_status = models.GoalStatus.objects.get(status_name = "Weekly Goal")),
                'dailyGoals': models.ScrumyGoals.objects.filter(goal_status = models.GoalStatus.objects.get(status_name = "Daily Goal")),
                'verifyGoals': models.ScrumyGoals.objects.filter(goal_status = models.GoalStatus.objects.get(status_name = "Verify Goal")),
                'doneGoals': models.ScrumyGoals.objects.filter(goal_status = models.GoalStatus.objects.get(status_name = "Done Goal"))}
    
    return render(request, 'umerahscrumy/home.html', context)