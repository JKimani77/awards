from django.db import models
from cloudinary.models import CloudinaryField
#import datetime as dt
from django.contrib.auth.models import User
from django.db.models.fields import TextField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = CloudinaryField('image')
    bio = TextField(blank=True)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)

    def save_profile(self):
        self.save()
    def del_profile(self):
        self.delete()

    @classmethod
    def get_profileid(cls,user):
        profile = cls.objects.filter(user=user).all()
        return Profile
    def updtprofile(self,bio):
        self.bio = bio
        self.save()

    
class Project(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=80)
    project_pic = CloudinaryField('project_picture')
    project_link = models.URLField()
    whenposted = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def save_proj(self):
        self.save()
    @classmethod
    def search_proj(cls, search_queri):
        projects = cls.objects.filter(title__icontains=search_queri)
        return projects
    @classmethod
    def get_projid(cls,id):
        project  = cls.objects.filter(id=id).all()
        return project

    @classmethod
    def get_user_projects(cls,profile):
        return cls.objects.filter(profile=profile)
    
    def updateproj(self, project_title):
        self.project_title = project_title
        self.save()
    def del_proj(self):
        self.delete()




class Review(models.Model):
    design = models.IntegerField()
    content = models.IntegerField()
    usability = models.IntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_review(self):
        self.save()


class Follow(models.Model):
    posted = models.DateTimeField(auto_now_add=True)
    followedd = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile_followed")
    followingg = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile_following")

    def __str__(self):
        return self.pk