from __future__ import unicode_literals

from django.db import models
# Create your models here.
class version_data(models.Model):
	version= models.SmallIntegerField(default= 0)
	compulsory_update= models.SmallIntegerField(default=0)
	ver_type=models.CharField(max_length=120, blank=True, null=True)
