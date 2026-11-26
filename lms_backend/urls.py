"""
URL configuration for lms_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from accounts.views import TrainerSignUpView,TrainerProfileRetrieveUpdateView

from rest_framework.authtoken.views import ObtainAuthToken

from course_management.views import CourseListCreateView,CourseRetrieveUpdateDeleteView

from module_management.views import ModuleCreateView,ModuleRetieveUpdateDelete

from lesson_management.views import LessonCreateView
from lesson_management.views import LessonRetriveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),

    #trainer
    path('trainer/signup/',TrainerSignUpView.as_view()),
    #profile
    path('trainer/profile/',TrainerProfileRetrieveUpdateView.as_view()),

    #token
    path('token/',ObtainAuthToken.as_view()),

    #course
    path('courses/',CourseListCreateView.as_view()),
    path('courses/<int:pk>/',CourseRetrieveUpdateDeleteView.as_view()),

    #module 
    path('course/<int:pk>/module/',ModuleCreateView.as_view()),
    path('module/<int:pk>/',ModuleRetieveUpdateDelete.as_view()),

    # lesson
    path("module/<int:pk>/lesson/",LessonCreateView.as_view()),
    path("lesson/<int:pk>/",LessonRetriveUpdateDestroyView.as_view()),

]
