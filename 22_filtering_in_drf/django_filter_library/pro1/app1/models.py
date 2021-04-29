from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=80)
    roll = models.IntegerField()
    city = models.CharField(max_length=80)
    added_by = models.CharField(max_length=80, default='admin')
