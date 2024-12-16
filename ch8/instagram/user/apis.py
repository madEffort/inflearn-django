from django.db import IntegrityError
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from user.models import CustomUser, Follow
from user.serializers import UserSignUpSerializer, UserMeReadSerializer, UserMeUpdateSerializer, FollowSerializer


class UserSignUpAPIView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSignUpSerializer


class UserMeAPIView(RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]  # 인증된 유저만 호출 가능하도록 설정
    authentication_classes = [JWTAuthentication]  # 인증 방식은 JWT로 설정

    def get_object(self):
        return self.request.user

    def get_serializer_class(self):
        if self.request.method == "GET":
            return UserMeReadSerializer
        elif self.request.method == "PATCH":
            return UserMeUpdateSerializer
        return super().get_serializer_class()


class UserFollowAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, *args, **kwargs):
        follow, _ = Follow.objects.get_or_create(user_id=kwargs["user_id"], follower_id=request.user.id)
        serializer = FollowSerializer(follow)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        Follow.objects.filter(user_id=kwargs["user_id"], follower_id=request.user.id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
