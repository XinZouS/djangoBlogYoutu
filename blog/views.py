# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView, 
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
)
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
	paginate_by = 5


class UserPostListView(ListView): # 某个用户的posts
	model = Post
	template_name = 'blog/user_posts.html' # url 模板<app>/<model>_<viewtype>.html, so
	context_object_name = 'posts'	# 然后告诉 home 调用的是 posts 对象
	ordering = ['-date_posted']		# 排序，加 - 号则逆序
	paginate_by = 5

	def get_queryset(self):
		# need: from django.shortcuts import render, get_object_or_404
		# and : from django.contrib.auth.models import User
		# kwargs is query arguments, here is the User obj:
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
	model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super(PostCreateView, self).form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super(PostUpdateView, self).form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False



def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})

