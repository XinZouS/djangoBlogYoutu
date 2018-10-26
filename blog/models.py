# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	# date_posted = models.DateTimeField(auto_now_add=True)
	# 上述auto_now_add不能修改这时间，所以用timezone包：
	date_posted = models.DateTimeField(default=timezone.now)
	# 用户创建，用外键，并关联删除，即若关联的用户被删了，全部Post也一起删；
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})


		