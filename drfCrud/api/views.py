from django.http import JsonResponse
from .serializers import StudentSerializer
from .models import Student
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
from django.views import View
from django.utils.decorators import method_decorator

################################################## Class based View ##################################################
@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return JsonResponse(serializer.data)
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg':'Data Created'})
    
    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get("id")
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg':'Data Updated'})
    
    def patch(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get("id")
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=pythondata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg':'Data Updated'})
        
    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get("id")
        stu = Student.objects.get(id=id)
        stu.delete()
        return JsonResponse({'msg':'Data Deleted'})


################################################## Function based View ##################################################


@csrf_exempt
def student_api(request):
    if request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return JsonResponse(serializer.data)
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg':'Data Created'})
    
    if request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get("id")
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg':'Data Updated'})
    
    if request.method == "PATCH":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get("id")
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=pythondata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg':'Data Updated'})
        
    if request.method == "DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get("id")
        stu = Student.objects.get(id=id)
        stu.delete()
        return JsonResponse({'msg':'Data Deleted'})