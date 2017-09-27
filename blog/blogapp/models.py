# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.encoding import  python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible

class Post(models.Model):

    author= models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)
    # blank = True implies data base validation allows null values to be true
    # null = True implies data base stores empty values as NULL in the data base


    def publish(self):

        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title




