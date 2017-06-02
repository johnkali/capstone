from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    third_name = models.CharField(max_length=100)
    id_number = models.IntegerField(default=0)  # generate 8digit random unique number
    district_of_birth = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    id_status = models.BooleanField(default=False)
    gender = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='person')

    def __str__(self):
        return str(self.id_number)


class Replacement(models.Model):
    first_name = models.CharField(max_length=100)
    id_number = models.ForeignKey(Person, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)
