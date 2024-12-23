from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from user import apis

urlpatterns = [
    path("", apis.UserSignUpAPIView.as_view(), name="user_sign_up"),
    path("login/", jwt_views.TokenObtainPairView.as_view(), name="user_login"),
    path("me/", apis.UserMeAPIView.as_view(), name="user_me"),
    path("<int:pk>/", apis.UserDetailView.as_view(), name="user_detail"),
    path("<int:pk>/follow/", apis.UserFollowAPIView.as_view(), name="user_follow"),
]
