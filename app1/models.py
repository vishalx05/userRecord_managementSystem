from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=10)
    contact = models.IntegerField()
    city=models.CharField(max_length=49)
    email=models.EmailField(max_length=49)


    def __str__(self):
        return self.name
