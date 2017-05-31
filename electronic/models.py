from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    third_name = models.CharField(max_length=100)
    id_number = models.IntegerField(default=0)
    district_of_birth = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=100)
    account = models.OneToOneField(User, on_delete=models.CASCADE, null=True)





