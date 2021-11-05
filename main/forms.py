from django.contrib.auth import forms
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Project, Review

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class UploadProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields=('name','description','author','image','linktosite')

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=("comment","rating") 



