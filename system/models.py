#coding:utf-8
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Info(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length = 100)
    birth = models.DateField()
    sex = models.CharField(max_length = 100,default='male')
    bSalary = models.FloatField()
    post = models.CharField(max_length = 100)
    department = models.ForeignKey('Department')
    def __unicode__(self):
        return self.name
    class Meta:
        permissions = (
                       ("super_permission", "Super permission"),
                    )
    
    
class Department(models.Model):
    dno = models.CharField(max_length = 100)
    manager = models.CharField(max_length = 100, default=None)
    def __unicode__(self):
        return self.dno


class Salary(models.Model):
    info = models.ForeignKey('Info')
    date = models.DateField()
    salary = models.FloatField()
    def __unicode__(self):
        return self.info.name
    class Meta:
        ordering = ['-date']
        permissions = (
                       ("update_salary", "Update salary"),
                       ("department_manager", "Department manager"),
                       ("HR_permission", "HR permission"),
                       )
    
class Check(models.Model):
    info = models.ForeignKey('Info')
    date = models.DateField()
    late = models.BooleanField(default=True)
    def __unicode__(self):
        return self.info.name

    class Meta:
        ordering = ['-date']
        permissions = (
                       ("department_manager", "Department manager"),
                       ("HR_permission", "HR permission"),
                       )
