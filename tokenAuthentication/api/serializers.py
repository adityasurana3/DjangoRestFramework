from .models import Student
from rest_framework import serializers

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'roll','city']