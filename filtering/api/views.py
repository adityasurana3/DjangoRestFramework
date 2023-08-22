from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSerializer

# Create your views here.
class StudentAPI(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get_queryset(self):
        return Student.objects.filter(passby=self.request.user)
    
