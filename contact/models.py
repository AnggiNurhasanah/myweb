from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Contact(models.Model):
    Email = models.CharField(max_length=30)
    Twitter = models.CharField(max_length=25)
    Github = models.CharField(max_length=15)
    NoHp = models.IntegerField()

    def __unicode__(self):
        return self.Email  1

    s                                                                                                                                                                                        