from __future__ import unicode_literals
from django.db import models

import re 
############################# LOGIN #############################

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Usermanager(models.Manager):
    def basic_validator(self,postData):
        errors= {}
        if len(postData['fname'])<2:
            errors['fname']='first name needed'
        if len(postData['lname'])<2:
            errors['lname']='last name needed'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email']='email required'
        if len(postData['password'])<8:
            errors['password']='password to short'
        if re.search('[A-Z]',postData['password']) is None:
            errors['password']='password needs one capital letter'
        if postData['password']!=postData['conpassword']:
            errors['password']="passwords dont match"
        return errors


    def login_validator(self, postData):
        errors={}
        try: #try to see if this is there.
            user = User.objects.get(email=postData['logemail'])
            if user.password == postData['logpassword']: # If this conditional returns true
                return errors #then do this
            else: #otherwise
                errors['logpassword'] = "Password is wrong"
                return errors
        except: #if you tried and failed. Quit      
            errors['logemail'] = "This email is invalid"
            return errors

class User(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=45)
    objects = Usermanager()
