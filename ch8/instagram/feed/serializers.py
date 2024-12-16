from rest_framework import serializers

from feed.models import Post, PostComment
from user.models import CustomUser


class PostSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source="user", read_only=True)

    class Meta:
        model = Post
        fields = ["id", "user_id", "image", "description", "created_at"]


class UserBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username"]


class CommentSerializer(serializers.ModelSerializer):
    user = UserBriefSerializer()
    replies = serializers.SerializerMethodField()  # 대댓글을 가져오기 위한 커스텀 필드

    class Meta:
        model = PostComment
        fields = ["id", "user", "parent_id", "content", "replies", "created_at"]

    def get_replies(self, obj):
        if obj.replies.exists():
            return CommentSerializer(obj.replies.all(), many=True).data
        return None


class PostDetailSerializer(serializers.ModelSerializer):
    user = UserBriefSerializer()
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ["id", "user", "image", "description", "comments", "created_at"]
