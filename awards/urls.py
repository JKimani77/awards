from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name = 'login'),
    path('createprofile/', views.make_profile, name = 'createprofile'),
    path('profile/<int:id>/', views.view_profile, name = 'myprofile'),
    path('post/',views.posting_project, name='post'),

]
