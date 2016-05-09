from __future__ import unicode_literals

from django.db import models


# Create your models here.

##### School Model #####
class school(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

##### Class Model #####
class classroom(models.Model):
    name = models.CharField(max_length=200)
    school = models.ForeignKey(school, on_delete=models.CASCADE, null=True)


##### Student Model #####
class student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    classroom = models.ForeignKey(classroom, on_delete=models.CASCADE, null=True)
