from django.db import models

class Department(models.Model):
    dept_name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    address_block = models.CharField(max_length=100)

    class Meta:
        db_table = 'department'

class Employee(models.Model):
    emp_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    dob = models.DateField()
    doj = models.DateField()
    gender = models.CharField(max_length=2)
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        db_table = 'employee'


