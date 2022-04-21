from django.shortcuts import render



from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from home.decorators import *
from django.contrib.auth.decorators import login_required

# Create your views here.



@login_required(login_url='home:LogIn')
@admin_only
def Faculty_Dashboard(request):
    return render(request, 'faculty/Faculty_dashboard.html')

@login_required(login_url='home:LogIn')
def Faculty_1(request):
    return render(request, 'faculty/Faculty_1.html')

@login_required(login_url='home:LogIn')
def Faculty_2(request):
    return render(request, 'faculty/Faculty_2.html')

@login_required(login_url='home:LogIn')
def Faculty_3(request):
    return render(request, 'faculty/Faculty_3.html')

@login_required(login_url='home:LogIn')

def Faculty_4(request):
    return render(request, 'faculty/Faculty_4.html')



@login_required(login_url='home:LogIn')
def Student_Dashboard(request):
    return render(request, 'student/StudentDashboard.html')

@login_required(login_url='home:LogIn')
def Student_1(request):
    return render(request, 'student/Student_1.html')
@login_required(login_url='home:LogIn')
def Student_2(request):
    return render(request, 'student/Student_2.html')
@login_required(login_url='home:LogIn')
def Student_3(request):
    return render(request, 'student/Student_3.html')

@login_required(login_url='home:LogIn')
def Student_4(request):
    return render(request, 'student/Student_4.html')




