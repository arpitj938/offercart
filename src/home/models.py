from __future__ import unicode_literals

from django.db import models

# Create your models here.
class city_data(models.Model):
	id= models.AutoField(Primary_Key= True)
	city_name= models.CharField(max_length=120, blank=True, null=True)

class category_data(models.Model):
	category_id = models.SmallIntegerField(Primary_Key= True)
	id= #
	category_name= models.CharField(max_length=120, blank=True, null= True)

class shop_data(models.Model):
	shop_id= models.SmallIntegerField(Primary_Key= True)
	id= #
	category_id= #
	shop_name= models.CharField(max_length=120, blank=True, null=True)


