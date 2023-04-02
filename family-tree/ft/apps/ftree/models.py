from django.db import models

# Create your models here.
class Ftree_Hierarchy(models.Model):
    key = models.IntegerField(null=False, unique=True)
    name = models.CharField(max_length=100, unique=False, null=False)
    title = models.CharField(max_length=100, unique=False, null=False)
    pic = models.CharField(max_length=100, unique=False, null=False)
    parent = models.IntegerField(unique=False, blank=True, null=True)
