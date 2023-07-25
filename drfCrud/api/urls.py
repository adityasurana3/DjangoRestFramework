from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.student_api),
    path('class', views.StudentAPI.as_view())
]
