from django.shortcuts import render
from django.http  import HttpResponse
from django.shortcuts import render,redirect
#from .forms import SignUpForm,LoginForm, ProfileForm, ProjectForm, RatingForm
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

# Create your views here.
