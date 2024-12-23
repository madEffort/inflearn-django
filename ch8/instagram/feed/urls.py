from django.urls import path

from feed import apis

urlpatterns = [
    path("posts/", apis.PostsAPIView.as_view(), name="posts"),
    path("posts/<int:pk>/", apis.PostDetailAPIView.as_view(), name="post_detail"),
    path("posts/<int:pk>/comments/", apis.PostCommentCreateAPIView.as_view(), name="post_comments"),
    path("comments/<int:pk>/", apis.PostCommentDestroyAPIView.as_view(), name="post_comment_detail"),
    path("posts/<int:pk>/like/", apis.PostLikeAPIView.as_view(), name="post_like"),
]
