from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('Profile/',profile,name='profile'),
    path('Settings/',settings,name='settings'),
    path('sign-in/',signIn,name='signIn'),
    path('sign-up/',signUp,name='signup'),
    path('Log-out/',logout,name='logout'),
    path('upload',upload,name='upload'),
    path('like-post',like_post,name='like-post'),
]