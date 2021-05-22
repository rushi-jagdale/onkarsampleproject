from django.db import models


# Create your models here.
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    title = models.CharField(max_length=25)
    Experience = models.IntegerField(blank=True, default=0)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Employee_details'


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=50)
    salary = models.IntegerField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.dept_name

    class meta:
        db_table = 'Dept_details'
