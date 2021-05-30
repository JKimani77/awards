from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile,Project,Review


class RegForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ('username','email', 'password1','password2')
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username',  max_length=254)
    password = forms.CharField(label='Password',widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('profile_pic','bio')

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('title','description','project_pic','project_link')

class RatingForm(forms.ModelForm):
    
    class Meta:
        model = Review
        
        fields =('design','usability','content')