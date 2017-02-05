from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
state = (
    ('Confirmed','Confirmed'),
    ('Pending','Pending'),
    ('FalseAlarm','FalseAlarm')
)
AGE_GROUP = (
    ('Child','Child'),
    ('Teen','Teenagers'),
    ('Adult','Adult'),
    ('Old','Old'),
)
class UserProfile(models.Model):
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name= 'userProfile'
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.IntegerField(max_length=10)
    city = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name+self.last_name

# currently service city
class City(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class HealthOfficer(models.Model):
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name= 'healthOfficer',
        blank=True, null=True
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.IntegerField(max_length=10)
    city = models.ManyToManyField(City,related_name='healthOfficer')
    def __str__(self):
        return self.first_name+self.last_name
    
class Query(models.Model):
    posted_by = models.ForeignKey(UserProfile,on_delete=models.CASCADE,blank=True, null=True)
    verified_by = models.ForeignKey(HealthOfficer,on_delete=models.CASCADE,blank=True, null=True)
    name = models.CharField(max_length=50)
    number_of_affected = models.IntegerField()
    # affected_area = models.CharField(max_length=50)
    affected_city = models.CharField(max_length=20)   # can be others
    number_of_casualties = models.IntegerField()
    status = models.CharField(max_length=20, choices=state)
    affected_age_group = models.CharField(max_length=20, choices=AGE_GROUP)
    posted_date = models.DateTimeField(auto_now_add=True)
    verified_date = models.DateTimeField(blank=True, null=True)
    precaution = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name

