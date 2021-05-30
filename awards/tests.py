from django.test import TestCase
from .models import Review,Project, Profile
from django.contrib.auth.models import User


class ReviewTestCase(TestCase):
    def setUp(self):
        self.user = User(username='memememe', email='mememe@gmail.com',password='112343')
        self.profile = Profile(profile_pic='/image/png',user=self.user,  bio=' bio bio bio')
        self.project = Project(title='Title of project', description='a blog web site',project_pic='/path/image.png',profile=self.profile)
        self.review = Review(design='9',usability='9',content='9',user=self.user,project=self.project)
        
    def test_save_review(self):
        self.user.save()
        self.profile.save()
        self.project.save()
        self.review.save_review()
        reviews = Review.objects.all()
        self.assertTrue(len(reviews) > 0)

class ProjectTestCase(TestCase):
    def setUp(self):
        self.new_user = User(username = 'newuser', password = '766578689', email = 'newuser@gmail.com')
        self.new_profile = Profile(user = 'newuser', profile_pic = '', bio = 'this is my new user bio')
        self.new_project = Project(title = 'my project title', description = 'this project does this commpression in this format', project_pic = '/image/png')

    def save_project(self):
        self.new_user.save()
        self.new_profile.save()
        self.new_project.save()
        new_project = Project.objects.all()
        self.assertTrue(len(new_project) > 0)

    def search_project(self):
        self.new_user.save()
        self.new_profile.save()
        self.new_project.save_proj()
        new_projj = self.new_project.search_proj('stuff')
        self.assertTrue(len(new_projj) > 0)
        

# Create your tests here.
