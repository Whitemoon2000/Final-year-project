from django.urls import path
from Game import views
from .views import (Login, Logout, Signup, home, profile)


app_name = 'Game'

urlpatterns = [
    path('login/',views.Login,name="Login"),
    path('logout/', views.Logout, name='Logout'),
    path('signup/',views.Signup,name="Signup"),
    path('home/',views.home,name="home"),
    path('profile/',views.profile,name="profile"),
]