"""pro1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from app1.views import StudentCreate, StudentDestroy, StudentList, StudentRetrieve, StudentUpdate
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from app1 import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# router.register('studentapi', views.StudentModelViewSet, basename='student')
# router.register('studentapiro', views.StudentReadOnlyModelViewSet,
#                 basename='studentreadonly')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hello/', views.Hello),
    # path('api/', views.StudentListandCreate.as_view()),
    # # path('create/', views.StudentCreate.as_view()),
    # path('retrive/<int:pk>', views.StudentRetrieve.as_view()),
    # path('update/<int:pk>', views.StudentUpdate.as_view()),
    # path('delete/<int:pk>', views.StudentDestroy.as_view()),
    # path('rud/<int:pk>', views.StudentRetrieveupdatedelete.as_view()),

    # generic api urls:
    path('stulist/', views.StudentList.as_view(), name='StudentList'),
    path('stucreate/', views.StudentCreate.as_view(), name='Studentcreate'),
    path('sturetrieve/<int:pk>', views.StudentRetrieve.as_view(),
         name='Studentretrieve'),
    path('stuupdate/<int:pk>', views.StudentUpdate.as_view(), name='Studentupdate'),
    path('studestroy/<int:pk>', views.StudentDestroy.as_view(),
         name='Studentdestroy'),

    # generic api with many combined:

    # path('listcreate/', views.StudentListCreate.as_view()),
    # path('retriveupdate/<int:pk>', views.StudentRetrieveUpdate.as_view()),
    # path('retriveupdatedestroy/<int:pk>',
    #      views.StudentRetrieveUpdateDestroy.as_view()),
    # path('retrivedestroy/<int:pk>', views.StudentRetrieveDestroy.as_view()),

    # path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),




]
