# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	# .CASCADE 是指当关联的User对象被删除时，此对象也一并删除
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	# default print func
	def __str__(self):
		return '%s Profile' % self.user.username

	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs) 
		# Python3 is: super().save()
		# When you are overriding model's save method in Django, you 
		# should also pass *args and **kwargs to overridden method. 

		img = Image.open(self.image.path)

		limitSize = 300
		if img.height > limitSize or img.width > limitSize:
			output_size = (limitSize, limitSize)
			img.thumbnail(output_size)
			img.save(self.image.path)


