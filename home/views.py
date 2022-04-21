from django.shortcuts import render



from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from home.decorators import *
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'home.html')

@admin_only
def Mainhome(request):
    return render(request, 'mainhome.html')




@unauthenticated_user
def LogIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
            
        user = authenticate(request, username=username, password=password) 
        if user is not None:
            login(request, user)
            return redirect('/Faculty_Dashboard')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return redirect('/LogIn')
    context = {} 
    return render(request, "login.html", context)
 
 
def logoutUser(request):
	logout(request)
	return redirect('home:LogIn')
