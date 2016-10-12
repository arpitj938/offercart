from __future__ import unicode_literals

from django.db import models

# Create your models here.
class mob_data(models.Model):
	id = models.DecimalField(default = 0)
	mob_no= models.DecimalField(max_digit= 10 , default= 0)

class user_data(models.Model):
	id = models.DecimalField(default= 0)
	name= models.CharField(max_length= 120,blank= True ,null = True)
	email= models.TextField(blank= True, null= True)




	 