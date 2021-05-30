from django.shortcuts import render
from django.http  import HttpResponse
from django.shortcuts import render,redirect
from .forms import RegForm,LoginForm
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


# Create your views here.
