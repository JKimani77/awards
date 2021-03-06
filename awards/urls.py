from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name = 'login'),
    path('createprofile/', views.make_profile, name = 'createprofile'),
    re_path('profile/(?P<id>\d+)/',views.view_profile,name = 'myprofile'),
    path('post/',views.posting_project, name='post'),
    path('logout/',views.logout_user, name='logout'),
    path('search/', views.search,name='search-project'),
    path('rating/<int:id>',views.review, name='rating'),
    path('api/profile/', views.ProfileList.as_view()),
    path('project/<int:id>',views.ratetotal,name='project-details'),
]

#