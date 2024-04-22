from django.db import models

# Create your models here.
class Signup(models.Model):
    name = models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=100)

    class Meta:
        db_table = 'users'
class Signin(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)