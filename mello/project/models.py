# project/models.py
# -*- coding: utf-8 -*-

from django.db import models

class Project(models.Model):
    name = models.CharField(max_length = 100, unique=True)

    def __str__(self):
        return self.name

    
