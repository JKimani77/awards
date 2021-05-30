from django.shortcuts import render
from django.http  import HttpResponse
from django.shortcuts import render,redirect
from .forms import RegForm,LoginForm,ProjectForm,ProfileForm
from django.contrib.auth import login,logout,authenticate
from .models import Profile, Project, Review
#from rest_framework.response import Response
#from rest_framework.views import APIView
from .models import Project
#from .serializers import ProjectSerializer,

# Create your views here.
def home(request):
    projects = Project.objects.all()

    return render(request, 'home.html',{'projects':projects})

def login(request):
    if request.method=='POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username,password=password)
            
            if user.is_active:
                login(request,user)
                return redirect(home)
            else:
                return "Your account is inactive"
    else:
        form = LoginForm()
    return render(request, 'auth/login.html',{"form":form})


def make_profile(request):
    joemama = request.user
    if request.method=="POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = joemama
            profile.save_profile()
            return redirect(home)
    else:
        form = ProfileForm()
    return render(request, 'createprofile.html',{"form":form})

def view_profile(request, id):
    joemama = request.user
    profile = Profile.objects.filter(user_id=id).all()
    projects = Project.objects.filter(profile=joemama.profile.id).all()
    return render(request, 'profile.html',{"profile":profile, "projects":projects})

def posting_project(request):
    joemama = request.user
    if request.method=="POST":
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = joemama.profile
            project.save_project()
            return redirect(home)
    else:
        form = ProjectForm()
    return render(request, 'newpost.html',{"form":form})