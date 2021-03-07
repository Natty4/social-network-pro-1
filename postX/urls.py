from django.urls import re_path, path, include
from . import views

urlpatterns = [

	path('', views.userPosts, name = 'posts'),
	path('<int:year>/<int:month>/<int:day>/<id>', views.postDetail, name = 'post_detail'),
	path('upload/', views.uploadPost, name = 'upload'),
	path('like/', views.postLike, name='like'),
	path('search/', views.postSearch, name='post_search'),
	path('delete/<pk>/', views.postDelete, name='post_delete'),
	#4 - CBV
	#path('up/', views.CreatePostView.as_view(), name='upl'),
	#path('ls/', views.PostListView.as_view(), name='ls'),
	#path('dt/<int:year>/<int:month>/<int:day>/<pk>/', views.PostDetailView.as_view(), name='dt'),
]