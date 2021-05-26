from django.forms import ModelForm, PasswordInput
from django.contrib.auth.models import User
from umerahscrumy.models import ScrumyGoals


class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password']
        widgets = {
            'password' : PasswordInput(),
        }



class CreateGoalForm(ModelForm):
    class Meta:
        model = ScrumyGoals
        fields = ['goal_name' , 'user']
