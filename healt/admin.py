from django.contrib import admin
from .models import Query,UserProfile,HealthOfficer,City

# Register your models here.

admin.site.register(Query)
admin.site.register(UserProfile)
admin.site.register(HealthOfficer)
admin.site.register(City)