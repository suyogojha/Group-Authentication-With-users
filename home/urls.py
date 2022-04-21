import imp
from django.urls import path
from home.views import *

app_name = "home"

urlpatterns = [
    path('', home, name='home'),
    path('LogIn/', LogIn, name='LogIn'),
    path("logoutUser/", logoutUser, name="logoutUser"),
    path("Mainhome/", Mainhome, name="Mainhome"),

]
