# coding:utf-8

from django.conf.urls import url
from .views import (
	PostListView, 	# home page show all blogs
	PostDetailView, # show one blog
	PostCreateView,	# new edit blog view
	PostUpdateView,
	PostDeleteView,
	UserPostListView
)
from . import views

urlpatterns = [
	# PopstListView 需要找url： <app>/<model>_<viewtype>.html	
	url(r'^$', PostListView.as_view(), name='blog-home'), 
	url(r'^user/(?P<username>[-\w]+)$', UserPostListView.as_view(), name='user-posts'),
	# 然后创建DetailView url，带参数id
	url(r'^post/(?P<pk>\d+)$', PostDetailView.as_view(), name='post-detail'), 
	# 然后创建CreateView url用于新建blog
	url(r'^post/new/$', PostCreateView.as_view(), name='post-create'), 
	# 然后创建UpdateView url用于更新blog
	url(r'^post/(?P<pk>\d+)/update/$', PostUpdateView.as_view(), name='post-update'),
	# 最后创建DeleteView
	url(r'^post/(?P<pk>\d+)/delete/$', PostDeleteView.as_view(), name='post-delete'),

	url(r'^about/$', views.about, name='blog-about'),
]

