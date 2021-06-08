from django.http  import Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

from .models import *
from .serializers import *
from .forms import LoginForm,ProjectForm,ProfileForm,RatingForm

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions 
# need


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
    return render(request, 'registration/login.html',{"form":form})

def logout_user(request):
    logout(request)
    return redirect(home)
    #

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
    
    current_user = request.user
    profile = Profile.objects.filter(user = id).all()
    #projects = Project.objects.filter(profile=current_user.profile.id).all()
    #project_count = projects.count()
    return render(request, 'profile.html',{"profile":profile}) #{"projects":projects})
    

@login_required(login_url="login/")

def posting_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        current_user=request.user
        try:
            profile = Profile.objects.get(user=current_user)
        except Profile.DoesNotExist:
            raise Http404("the user profile does not exist")
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = profile
            project.save()
        return redirect('home')
    else:
        form=ProjectForm()
    return render(request, 'newpost.html',{"form": form })#"project":project

#
def search(request):
    if 'project'in request.GET and request.GET['project']:
        search_project = request.GET.get('project')
        searched = Project.search_proj(search_project)
        message = f'{search_project}'
        return render(request, 'search.html',{"projects":searched, "message":message})
    
def review(request, id):
    current_user = request.user
    project = Project.objects.get(pk=id)
    rating = Review.objects.filter(project=project.id).all()
    if request.method=='POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = current_user
            rating.project = project
            rating.save_review()
            return redirect(home)
        
    else:
        form = RatingForm()
    return render(request, 'rating.html', {"form":form, "project":project, "ratings":rating})

def ratetotal(request,id):
    project = Project.objects.get(pk=id)
    ratings = Review.objects.filter(project=project.id).all()
    design = Review.objects.filter(project=project.id).values_list('design',flat=True)
    usability = Review.objects.filter(project=project.id).values_list('usability',flat=True)
    content = Review.objects.filter(project=project.id).values_list('content',flat=True)
    total_design=0
    total_usability=0
    total_content = 0
    for score in design:
        total_design+=score
    for score in usability:
        total_usability+=score
    for score in content:
        total_content+=score
        
        
    total_score = (total_design + total_usability + total_content)/3
    return render(request, 'ratingtotal.html',{"project":project, "ratings":ratings,"total_score":total_score})

class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)       
        return Response(serializers.data)



@permission_classes((permissions.AllowAny,))
class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

    



































































































































































































































































































































































































































































































































































































































































































#def posting_project(request):
    #joemama = request.user
    #if request.method=="POST":
        #form = ProjectForm(request.POST,request.FILES)
        #if form.is_valid():
            #project = form.save(commit=False)
            #rin)
            #project.profile = joemama.profile
            #project.save_proj()
            #return redirect(home)
    #else:
        #form = ProjectForm()
    #return render(request, 'newpost.html',{"form":form})
