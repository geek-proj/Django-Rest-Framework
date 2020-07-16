from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Fields(models.Model):
	user  = models.ForeignKey(User,related_name='fields',on_delete=models.CASCADE)
	date_added  = models.DateTimeField(default=now,editable=False)
	name     = models.CharField(max_length=100)
	value    = models.CharField(max_length=100)
	def __str__(self):
		return '{},{}'.format(name,value)


