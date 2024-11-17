from django.urls import path
from . import views

urlpatterns = [
     path('home',views.home,name="home"),
     path('register',views.register,name="register"),
     path('main',views.main,name="main"),
     path('createcourse',views.createcourse,name="createcourse"),
     path('createaccounts',views.createaccounts,name="createaccounts"),
     path('studentaccounts',views.studentaccounts,name="studentaccounts"),
     path('staffaccounts',views.staffaccounts,name="staffaccounts"),
    path('studentcourse',views.studentcourse,name="studentcourse"),
    path('resetpassword',views.resetpassword,name="resetpassword"),
    path('studentpassword',views.studentpassword,name="studentpassword"),
    path('staffpassword',views.staffpassword,name="staffpassword"),
    path('studentlogin/', views.student_login, name='studentlogin'),
    path('acadamicspage', views.acadamicspage, name='acadamicspage'),
    path('studentpage', views.studentpage, name='studentpage'),
   
]
