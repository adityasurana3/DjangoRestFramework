from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


# Create your views here.
class StudentAPI(viewsets.ViewSet):
    def list(self, request):
        student = Student.objects.all()
        serailizer = StudentSerializer(student, many=True)
        return Response(serailizer.data)
    
    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        
    def update(self, request, pk):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data Updated'})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Partial Data Updated'})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            stu.delete()
            return Response({'msg':'Data Deleted'},status=status.HTTP_204_NO_CONTENT)