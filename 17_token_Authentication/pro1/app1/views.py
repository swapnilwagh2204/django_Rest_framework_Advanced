
# import json
# from django.http.response import JsonResponse
# from django.shortcuts import render
# import io
# from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer
# Create your views here.
import rest_framework
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
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly


#viewset in django
from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes=[AllowAny]
    # permission_classes=[IsAdminUser]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    # for djangomodelpermissions..we need to give permissions from admin page
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    # non  authenticated banda read kar payega
    # aur jo authenticated hai us bande ko ham permission de sakte hai
    # if we want this classses globally..we can write this in setting.py
