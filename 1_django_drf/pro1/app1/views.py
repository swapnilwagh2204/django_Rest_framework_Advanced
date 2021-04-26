from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


def student_details(request, id):
    stu = Student.objects.get(id=id)
    serializer = StudentSerializer(stu)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type="application/json")
    return JsonResponse(serializer.data, safe=True)

# all students data  queryset


def student_list(request):
    stu = Student.objects.all()
    print(type(stu))
    serializer = StudentSerializer(stu, many=True)
    print(type(serializer))
    json_data = JSONRenderer().render(serializer.data)
    print(type(json_data))
    return HttpResponse(json_data, content_type="application/json")
