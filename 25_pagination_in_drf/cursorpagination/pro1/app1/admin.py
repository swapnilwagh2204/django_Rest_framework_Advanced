from .models import Student
from django.contrib import admin

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city', 'added_by']


admin.site.register(Student, StudentAdmin)
