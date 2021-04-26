from .models import Student
from rest_framework import serializers


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=80)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=80)

    def create(self, validate_data):
        return Student.objects.create(**validate_data)
