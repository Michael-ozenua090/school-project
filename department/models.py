from django.db import models

# Create your models here. Department models


class Department(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.code
    



