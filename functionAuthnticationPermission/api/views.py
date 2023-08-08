from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication


# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def StudentAPI(request, pk = None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Created"})
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Hello"})
        return Response({"msg":"Error"})
    
    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({"msg":"Deleted"})
