from django.db import models





class Student(models.Model):
    Name = models.CharField(max_length=20)
    Mobile = models.CharField(max_length=10)
    Email = models.EmailField(max_length=25)
    password=models.CharField(max_length=15)
    City = models.CharField(max_length=10)
    State = models.CharField(max_length=20)
    Gender_choice = [('male', 'male'), ('female', 'female')]
    Gender = models.CharField(max_length=20, choices=Gender_choice)


class ramkrishna(models.Model):
    Email = models.EmailField(max_length=30)
    password = models.CharField(max_length=15)

class delete(models.Model):
    Email = models.EmailField(max_length=30)