from django.urls import path
from . import views
app_name='blog'
 
urlpatterns=[
	path('',views.PostList.as_view(),name='index'),
	path('post/<int:pk>/',views.PostDetail.as_view(),name='detail'),
	path('post/new/',views.PostCreate.as_view(),name='create'),
	path('post/edit/<int:pk>/',views.PostUpdate.as_view(),name='update'),
	path('post/delete/<int:pk>/',views.PostDelete.as_view(),name='delete'),
	#path('comment/<int:pk>/',views.comment,name='comment'),
	path('comment/<int:pk>/',views.PostDetail.as_view(),name='comment'),
	path('publish/<int:pk>/',views.publish,name='publish'),
	path('drafts/',views.DraftList.as_view(),name='drafts'),
	path('save_draft/<int:pk>',views.save_draft,name='save_draft'),
	path('my_posts/',views.MyPostList.as_view(),name='my_posts'),
]