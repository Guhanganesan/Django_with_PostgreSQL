from django.db import models

# Create your models here.

class Employee(models.Model):
    EmpId = models.CharField(max_length=5)
    EmpName = models.CharField(max_length=200)
    EmpGender = models.CharField(max_length=10)
    EmpEmail = models.EmailField()
    EmpDesignation = models.CharField(max_length=150)
    class Meta:
        db_table="Employee"

# The created table contains an auto-created id field
class EceStudents(models.Model):
    std_age =  models.IntegerField()
    std_email = models.CharField(max_length=200)
    std_pass_word = models.CharField(max_length=200)
    class Meta:
        db_table="EceStudents"

class CseStudents(models.Model):
    name = models.CharField(max_length=100)
    age =  models.IntegerField()
    email = models.CharField(max_length=200)
    pass_word = models.CharField(max_length=200)
    class Meta:
        db_table="CseStudents"