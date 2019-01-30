from __future__ import unicode_literals
from django.db import models
from apps.login.models import User


class Jobmanager(models.Manager):
    def job_validator(self,postData):
        errors= {}
        if len(postData['title'])<3:
            errors['title']='Title needs to be ateast 3 letters'
        if len(postData['desc'])<3:
            errors['desc']='Description needs to be atleast 3 letters'
        if len(postData['location'])<3:
            errors['location']='Location needs to be atleast 3 letters'
        return errors

class Job(models.Model):
    user = models.ForeignKey(User,related_name='job')
    title = models.CharField(max_length=225)
    desc = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=225)
    objects = Jobmanager()