import io
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse


# def student_details(request, id):
#     stu = Student.objects.get(id=id)
#     serializer = StudentSerializer(stu)
#     # json_data = JSONRenderer().render(serializer.data)
#     # return HttpResponse(json_data, content_type="application/json")
#     return JsonResponse(serializer.data, safe=True)

# # all students data  queryset


# def student_list(request):
#     stu = Student.objects.all()
#     print(type(stu))
#     serializer = StudentSerializer(stu, many=True)
#     print(type(serializer))
#     json_data = JSONRenderer().render(serializer.data)
#     print(type(json_data))
#     return HttpResponse(json_data, content_type="application/json")

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data inserted'}
            json_data = JSONRenderer().render(res)
        else:
            json_data = JSONRenderer().render(serializer.errors)

        print("hello")
        return HttpResponse(json_data, content_type='application/json')
