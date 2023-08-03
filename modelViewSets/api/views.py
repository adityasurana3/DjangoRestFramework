from django.shortcuts import render
from .models import Student
from .serailizers import StudentSerializer
from rest_framework import viewsets

# Create your views here.
class StudentAPI(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer