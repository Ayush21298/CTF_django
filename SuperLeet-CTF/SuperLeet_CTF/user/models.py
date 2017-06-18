from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=200)
    username=models.CharField(max_length=32)
    email=models.EmailField(max_length=256)
    password=models.CharField(max_length=32)
    admin=models.BooleanField(default=False)

class Question(models.Model):

    # def __init__(self, arg):
    #     super(Question, self).__init__()
    #     self.arg = arg

    que=models.CharField(max_length=256)
    options = JSONField()
