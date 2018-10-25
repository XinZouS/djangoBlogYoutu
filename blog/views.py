# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html' # url 模板<app>/<model>_<viewtype>.html, so
	context_object_name = 'posts'	# 然后告诉 home 调用的是 posts 对象
	ordering = ['-date_posted']		# 排序，加 - 号则逆序

class PostDetailView(DetailView):
	model = Post


def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})

