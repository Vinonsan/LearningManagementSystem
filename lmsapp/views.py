
from django.shortcuts import render

from .models import *


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

def studentpassword(request):
    student=Student.objects.all()
    context={'student': student}
    return render(request,"lms/student_password.html",context)

def staffpassword(request):
    staff=Staff.objects.all()
    context={'staff': staff}
    return render(request,"lms/staff_password.html",context)