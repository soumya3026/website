
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser

class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = MyUser
        fields = ('is_student','is_faculty')

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = MyUser
        fields = ('is_student','is_faculty')