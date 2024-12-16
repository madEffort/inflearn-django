import os
import uuid

from django.db import models

from user.models import CustomUser


def unique_file_path(instance, filename):
    ext = filename.split(".")[-1]  # 확장자 추출
    filename = f"{uuid.uuid4()}.{ext}"  # 고유 파일명 생성
    return os.path.join("posts/images/", filename)


class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="posts")
    image = models.ImageField(upload_to=unique_file_path)
    description = models.TextField(blank=True)  # 게시물 설명
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]  # 최신순 정렬


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("post", "user")  # 한 유저는 같은 게시물에 여러 번 좋아요 누를 수 없음


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", null=True, on_delete=models.CASCADE, related_name="replies")
    content = models.CharField(max_length=200)  # 댓글 내용
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]
