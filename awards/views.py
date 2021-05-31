from django.http  import Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponse
from .forms import LoginForm,ProjectForm,ProfileForm,RatingForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import Profile, Project, Review
#from rest_framework.response import Response
#from rest_framework.views import APIView
#from .serializers import ProjectSerializer,ProfileSerialiser
#from rest_framework.views import APIView


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

def logout_user(request):
    logout(request)
    return redirect(home)

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
    
    #current_user = request.user
    profile = Profile.objects.filter(user_id = id).all()
    #projects = Project.objects.filter(profile=current_user.profile.id).all()
    #project_count = projects.count()
    return render(request, 'profile.html',{"profile":profile}) #{"projects":projects})

@login_required(login_url="login/")
def posting_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
           
            project = form.save(commit=False)
            project.user = request.user
            profileid = Profile.objects.filter(id).update() 
            project.save()
            return redirect('home')
                     #projectx = Project()
            #projectx.user = current_user
            #projectx.save_proj()
            
    else:
        form=ProjectForm()
    return render(request, 'newpost.html',{"form": form })#"project":project

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


#class ProjectList(APIView):
    #def get(self, request, format=None):
        #all_projects = Project.objects.all()
        #serializers = ProjectSerializer(all_projects, many=True)
        #return Response(serializers.data)
    
#class ProfileList(APIView):
    #def get(self, request, format=None):
        #all_profiles = Profile.objects.all()
        #serializers = ProfileSerializer(all_profiles, many=True)
        #return Response(serializers.data)



































































































































































































































































































































































































































































































































































































































































































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
