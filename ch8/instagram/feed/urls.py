from django.urls import path

from feed import apis

urlpatterns = [
    path("", apis.PostsAPIView.as_view(), name="posts"),
    path("<int:pk>/", apis.PostDetailAPIView.as_view(), name="post_detail"),
]
