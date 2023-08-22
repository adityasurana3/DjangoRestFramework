from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class StudentAPI(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    ################################### Method 1 without using any library ###################################
    # def get_queryset(self):
    #     return Student.objects.filter(passby=self.request.user)
    
    ################################### Method 2 using django-filters ###################################
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','city']


    
