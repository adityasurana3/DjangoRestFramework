from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from .models import Student
from .serializers import StudentSerializers

# Create your views here.
class StudentAPI(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    authentication_classes = [SessionAuthentication]
    # User must have the permission to do the task if he need to post the data User must have Add permission for update change_permission and for delete delete_permission. Permission can be given from admin panel or you can code to give the particular permission
    # permission_classes = [DjangoModelPermissions] # User must be loggedin to access the api even read access is not given
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly] # If the user is not logged in he will be given read access
    