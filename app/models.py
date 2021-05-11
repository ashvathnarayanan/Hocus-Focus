from django.db import models

class Trigger(models.Model):
    name  = models.CharField(blank=False,max_length=100)
    lang  = models.CharField(blank=False,max_length=100)

class Question(models.Model):
    course  = models.CharField(blank=False,max_length=100)
    number  = models.CharField(blank=False,max_length=100)
    content = models.CharField(blank=True,max_length=100)
    answer  = models.CharField(blank=True,max_length=100)

class Student(models.Model):
    regno   = models.CharField(blank=False,max_length=100)
    score   = models.PositiveIntegerField(blank=False, null=False)
