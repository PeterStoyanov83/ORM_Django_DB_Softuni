from django.db import models


# Create your models here.

class MyModel(models.Model):
    task_title = models.CharField(max_length=50)
    task_text = models.TextField()


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)

