from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttling import CustomRateThrottle


# Create your views here.

class StudentAPI(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    throttle_classes = [AnonRateThrottle, CustomRateThrottle]
