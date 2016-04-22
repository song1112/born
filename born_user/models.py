from __future__ import unicode_literals

from django.db import models

class user(models.Model):
    createdate = models.DateTimeField(auto_now_add=True)
    updatedate = models.DateTimeField(auto_now=True)
    account = models.CharField(blank=False, max_length=20, unique=True)
    password = models.CharField(blank=False, max_length=20)
    name = models.CharField(blank=True, null=True, max_length=20, default="")
    nickname = models.CharField(blank=True, null=True, max_length=20, default="")
    sex = models.CharField(blank=True, null=True, max_length=2, default="")
    birthday = models.DateField(null=True)
    email = models.EmailField(unique=True)

