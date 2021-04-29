
# import json
# from django.http.response import JsonResponse
# from django.shortcuts import render
# import io
# from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer
# Create your views here.
from rest_framework.filters import SearchFilter
import rest_framework
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from .models import Student
from . serializers import StudentSerializer
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.views.generic.base import View
# from django.utils.decorators import method_decorator
# # '''
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status

# # generic api view
# # concrete rest api views:

# import rest_framework.generics
# from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin

# from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView


# rest_authentication
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly


# viewset in django
from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets

# throttling classes in rest_framework
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
# from app1.customthrottle import dummythrottle
from rest_framework.throttling import ScopedRateThrottle

from rest_framework.filters import OrderingFilter

# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     authentication_classes = [SessionAuthentication]
#     # permission_classes = [IsAuthenticated]
#     # permission_classes=[AllowAny]
#     # permission_classes=[IsAdminUser]
#     permission_classes = [IsAuthenticatedOrReadOnly]
# permission_classes = [DjangoModelPermissions]
# for djangomodelpermissions..we need to give permissions from admin page
# permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
# non  authenticated banda read kar payega
# aur jo authenticated hai us bande ko ham permission de sakte hai

# if we want this classses globally..we can write this in setting.py
# throttle_classes = [AnonRateThrottle, UserRateThrottle]
# throttle_classes = [AnonRateThrottle, dummythrottle]
# other settings in settings.py files


'''
# modellviewset and readonlymodelviewset

class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class StudentModelSerializer(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


'''

# viewset in django
'''

class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):

        print("Description:", self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'})
        return Response(serializer.errors)

    def destroy(self, request, pk):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data Deleted'})

'''

# concrete views:


# class StudentListCreate(ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# class StudentRetrieveUpdate(RetrieveUpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# class StudentRetrieveDestroy(RetrieveDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# generic views:


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # throttle_classes = [ScopedRateThrottle]
    # throttle_scope = 'stulist'

    # def get_queryset(self):
    #     user = self.request.user
    #     print(user)
    #     return Student.objects.filter(added_by=user)

    filter_backends = [SearchFilter]
    search_fields = ['name', 'city']
    # search_fields = ['^name']

    # ordering:
    filter_backends = [OrderingFilter]  # sabse ordering hota hai
    ordering_fields = ['name', 'city' ]


class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # throttle_classes = [ScopedRateThrottle]
    # throttle_scope = 'sturetrive'


class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


'''
# Generic api views: many in one combined


class StudentListandCreate(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)  # here we get the list

    def post(self, request, *args, **kwargs):
        # here create the data..insert
        return self.create(request, *args, **kwargs)


class StudentRetrieveupdatedelete(GenericAPIView, RetrieveModelMixin, UpdateModelMixin,  DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)  # here we get the list

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)  # here we get the list

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)  # here we get the list


'''
'''
# generic api views: individual


class StudentList(GenericAPIView, ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)  # here we get the list


class StudentCreate(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        # here create the data..insert
        return self.create(request, *args, **kwargs)


class StudentRetrieve(GenericAPIView, RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)  # here we get the list


class StudentUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)  # here we get the list


class StudentDestroy(GenericAPIView, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)  # here we get the list


'''
'''
# api views


class student_api(APIView):
    def get(self, request, pk=None, form=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)

        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data is added'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'complete data is updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'partial data is updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg': 'data is deleted'})


'''


'''
# traditionoal way


@method_decorator(csrf_exempt, name='dispatch')
class student_api(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data created successfully'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        print(id)
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data updated successfully'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        print(id)
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'Data deleted successfully'}
        return JsonResponse(res, safe=True)
        # json_data = JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data, content_type='application/json')
'''
