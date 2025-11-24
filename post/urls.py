from django.urls import path

from post.views import PostDetailAPIView, PostListView

app_name = 'post'

urlpatterns = [
    path('', PostListView.as_view(), name='get_post_detail'),
    path('/<int:post_id>', PostDetailAPIView.as_view(), name='get_post_detail'),
]
