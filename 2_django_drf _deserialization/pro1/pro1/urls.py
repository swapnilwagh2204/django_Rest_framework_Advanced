
from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('stuinfo/<int:id>', views.student_details),
    # path('stulist/', views.student_list),
    path('stuadd/', views.student_create),
]
