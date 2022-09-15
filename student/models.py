from django.db import models

from department.models import Department

# Create your models here. Students models


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    regno = models.CharField(max_length=6, unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)




    def __str__(self):
        return self.first_name
    
