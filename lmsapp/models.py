from django.db import models

# Create your models here.
from django.db import models
import datetime
import os

# Create your models here.

def getFileName(request,filename):
    now_time=datetime.datetime.now().strftime("%y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads',new_filename)

class Course(models.Model):
    Course_Name=models.CharField(max_length=150,null=False,blank=False)
    Course_Code=models.CharField(max_length=150,null=False,blank=False,primary_key=True)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    description=models.TextField(max_length=500,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def _str_(self) :
        return self.name
    

class Staff(models.Model):
    Staff_image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    Staff_Name=models.CharField(max_length=150,null=False,blank=False)
    Staff_User_Name=models.CharField(max_length=150,null=False,blank=False)
    email = models.EmailField(max_length=50, unique=True)
    Staff_Identity_Number=models.CharField(max_length=150,null=False,blank=False,primary_key=True)
    Staff_NIC_Number=models.CharField(max_length=150,null=False,blank=False)
    Staff_Phone_Number=models.CharField(max_length=150,null=False,blank=False)
    Staff_Password=models.CharField(max_length=100)
    
    def _str_(self) :
        return self.name
    
class Student(models.Model):
    Student_image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    Student_Name=models.CharField(max_length=150,null=False,blank=False)
    Student_User_Name=models.CharField(max_length=150,null=False,blank=False)
    Student_email = models.EmailField(max_length=50, unique=True)
    Student_Registration_Number=models.CharField(max_length=150,null=False,blank=False,primary_key=True)
    Student_Admission_Number=models.CharField(max_length=150,null=False,blank=False)
    Student_NIC_Number=models.CharField(max_length=150,null=False,blank=False)
    Student_Phone_Number=models.CharField(max_length=150,null=False,blank=False)
    Student_Password=models.CharField(max_length=100)
   
    
    def _str_(self) :
        return self.name
    
SUBJECT_CHOICES = (
   ('CS', 'Computer Science'),
   ('M', 'Maths'),
   ('B', 'Biology'),
   ('P', 'Physics'),
)

DEPARTMENT= (
   ('PY', 'Physical Science'),
   ('BS', 'biological Science'),
   ('ICT', 'Information Communication Technology'),
   ('HPT', 'Health Promotion'),
)

class Student_Course(models.Model):
    Student=models.ForeignKey(Student,on_delete=models.CASCADE)
    Registered_Courses = models.CharField(choices=SUBJECT_CHOICES, max_length=128)
    Student_date_of_birth = models.DateTimeField()
    Department = models.CharField(choices=DEPARTMENT, max_length=128)

    
    def _str_(self) :
        return self.name