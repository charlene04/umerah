from django.contrib import admin

# Register your models here.
from . models import ScrumyGoals
from . models import ScrumyHistory
from . models import GoalStatus
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(ScrumyGoals)
admin.site.register(ScrumyHistory)
admin.site.register(GoalStatus)