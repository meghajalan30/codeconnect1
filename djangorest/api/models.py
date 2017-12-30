from __future__ import unicode_literals
from django.db import models
# Create your models here.


class UserInfo(models.Model):
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=20,unique='true')
    email=models.CharField(max_length=20,unique='true')
    password=models.CharField(max_length=20)
    hackerrank=models.CharField(max_length=20,unique='true')
    codeforces=models.CharField(max_length=20,unique='true')
    about=models.CharField(max_length=200)
