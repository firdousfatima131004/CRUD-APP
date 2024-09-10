from django.db import models

class Crudprofiles(models.Model):
    username=models.CharField(max_length=12)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)