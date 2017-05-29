from django.db import models
from django.db.models.signals import post_save

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    third_name = models.CharField(max_length=100)
    id_number = models.IntegerField()
    district_of_birth = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=50)
    gender = models.BooleanField()




"""
def create_profile(sender,**kwargs):
    if kwargs('created'):
        user_profile = Person.objects.create(user=kwargs('instance'))

post_save.connect(create_profile, sender=user)

*registration
*login
*get_new_id
*replace_id
*id_status


"""

#
