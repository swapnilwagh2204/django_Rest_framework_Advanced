from django.http import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def Hello(request):
    if request.method == 'GET':
        print(request.data)
        return Response({'msg': 'this is get api'})
    if request.method == 'POST':
        print(request.data)
        return Response({'msg': 'this is POST api'})

# class student_api(View):
#     def get(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id', None)
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type='application/json')
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type='application/json')
#     def post(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = StudentSerializer(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data created successfully'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
#     def put(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         print(id)
#         stu = Student.objects.get(id=id)
#         serializer = StudentSerializer(stu, data=pythondata, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data updated successfully'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
#     def delete(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         print(id)
#         stu = Student.objects.get(id=id)
#         stu.delete()
#         res = {'msg': 'Data deleted successfully'}
#         return JsonResponse(res, safe=True)
#         # json_data = JSONRenderer().render(serializer.errors)
#         # return HttpResponse(json_data, content_type='application/json')
