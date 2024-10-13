from django.urls import path

from .apps import BlogConfig
from .views import BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogPostListView.as_view(), name='post_list'),
    path('<int:pk>/', BlogPostDetailView.as_view(), name='post_detail'),
    path('create/', BlogPostCreateView.as_view(), name='post_create'),
    path('<int:pk>/edit/', BlogPostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', BlogPostDeleteView.as_view(), name='post_delete'),
]
