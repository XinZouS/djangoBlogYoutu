# coding:utf-8

from django.conf.urls import url
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
	url(r'^$', PostListView.as_view(), name='blog-home'), # PopstListView 需要找url： <app>/<model>_<viewtype>.html	
	url(r'^post/(?P<pk>\d+)', PostDetailView.as_view(), name='post-detail'), # 然后创建DetailView url，带参数id
	url(r'^about/$', views.about, name='blog-about'),
]

