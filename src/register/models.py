from __future__ import unicode_literals

from django.db import models

# Create your models here.

class user_data(models.Model):
	id = models.SmallIntegerField(primary_key= True,default= 0)
	name= models.CharField(max_length= 120,blank= True ,null = True)
	email= models.TextField(blank= True, null= True)
	city= models.CharField(max_length=120, blank=True, null=True)
	mobile=models.DecimalField(max_digits=10,decimal_places=0)




	 