from django.db import models
from datetime import datetime

class User(models.Model):
    ''' '''
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined = models.DateField(default=datetime.now())

    def __str__(self):
        '''Dunder method to overwrite how model data is displayed'''
        return self.firstName + ' ' + self.lastName

class pet(models.Model):
    ''' '''
    name = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
