from __future__ import unicode_literals

from django.db import models
# Create your models here.
class version_control(models.Model):
	version_no= models.SmallIntegerField(default= 0)
	compulsory_update= models.SmallIntegerField(default=0)
