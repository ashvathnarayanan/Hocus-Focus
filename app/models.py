from django.db import models

class Trigger(models.Model):
    name  = models.CharField(blank=False,max_length=100)

class Student(models.Model):
    trigger = models.ForeignKey(Trigger,on_delete=models.CASCADE)
    regno = models.CharField(blank=False,max_length=100)
    score = models.PositiveIntegerField(blank=False, null=False)
