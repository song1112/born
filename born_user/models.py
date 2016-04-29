from __future__ import unicode_literals

from django.db import models

import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible
from django.conf import settings
@deconstructible
class PathAndRename(object):
    def __init__(self, path):
        self.sub_path = path
    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.sub_path, filename)

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

class project(models.Model):
    createdate = models.DateTimeField(auto_now_add=True)
    updatedate = models.DateTimeField(auto_now=True)
    user_id = models.IntegerField()
    music_id = models.IntegerField()

class music(models.Model):
    createdate = models.DateTimeField(auto_now_add=True)
    updatedate = models.DateTimeField(auto_now=True)
    name = models.CharField(blank=False, max_length=20)
    category = models.CharField(blank=False, max_length=20)
    source = models.FileField(upload_to=PathAndRename('music/'))

class MusicFile(models.Model):
    musicfile = models.FileField(upload_to=PathAndRename('testmusic/'))
