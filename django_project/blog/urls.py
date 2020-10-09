from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'), # blog/user_posts.html

    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'), # blog/post_detail.html
    path('post/new/', PostCreateView.as_view(), name='post-create'), # blog/post_form.html
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'), # blog/post_form.html
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'), # blog/post_confirm_delete.html
    
    path('about/', views.about, name='blog-about'),
]