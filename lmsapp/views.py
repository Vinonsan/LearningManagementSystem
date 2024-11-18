
from django.shortcuts import render

from .models import *

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from lmsapp.models import Student


# Create your views here.
def home(request):
    return render(request,"lms/index.html")
def register(request):
    return render(request,"lms/register.html")
def main(request):
    return render(request,"lms/admin.html")

def createcourse(request):
    course=Course.objects.all()
    context={'course': course}
    return render(request,"lms/create_course.html",context)
    
def createaccounts(request):
    return render(request,"lms/create_accounts.html")
def studentaccounts(request):
    student=Student.objects.all()
    context={'student': student}
    return render(request,"lms/student_account.html",context)

def staffaccounts(request):
    staff=Staff.objects.all()
    context={'staff': staff}
    return render(request,"lms/staff_accounts.html",context)

def studentcourse(request):
    studentcourse=Student_Course.objects.all()
    context={'studentcourse': studentcourse}
    return render(request,"lms/studentcourse.html",context)


def resetpassword(request):
    return render(request,"lms/resetpassword.html")

def acadamicspage(request):
    return render(request,"lms/acadamicspage.html")

def acadamicsresult(request):
    return render(request,"lms/acadamicsresult.html")

def studentviewcourse(request):
    student2=Student.objects.all()
    context={'student': student2}
    return render(request,"lms/studentviewcourse.html")

def studentpage(request):
    return render(request,"lms/studentpage.html")

def studentpassword(request):
    student=Student.objects.all()
    context={'student': student}
    return render(request,"lms/student_password.html",context)

def staffpassword(request):
    staff=Staff.objects.all()
    context={'staff': staff}
    return render(request,"lms/staff_password.html",context)

def student_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate user with custom model
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # Login the user and redirect to the dashboard or home
            return redirect('dashboard')  # Make sure 'dashboard' is a valid URL name
        else:
            # If authentication fails, show an error message
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'studentlogin.html') 