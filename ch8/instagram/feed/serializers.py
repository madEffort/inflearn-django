from rest_framework import serializers

from feed.models import Post, PostComment, PostLike
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


class PostCommentSerializer(serializers.ModelSerializer):
    user = UserBriefSerializer()
    replies = serializers.SerializerMethodField()  # 대댓글을 가져오기 위한 커스텀 필드

    class Meta:
        model = PostComment
        fields = ["id", "user", "parent_id", "content", "replies", "created_at"]

    def get_replies(self, obj):
        if obj.replies.exists():
            return PostCommentSerializer(obj.replies.all(), many=True).data
        return None


class PostDetailSerializer(serializers.ModelSerializer):
    user = UserBriefSerializer()
    comments = PostCommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ["id", "user", "image", "description", "comments", "created_at"]


class PostCommentCreateSerializer(serializers.ModelSerializer):
    post_id = serializers.PrimaryKeyRelatedField(source="post", queryset=Post.objects.all())
    user_id = serializers.PrimaryKeyRelatedField(source="user", read_only=True)
    parent_id = serializers.PrimaryKeyRelatedField(source="parent", queryset=PostComment.objects.all(), required=False)

    class Meta:
        model = PostComment
        fields = ["id", "post_id", "user_id", "parent_id", "content", "created_at"]

    def validate(self, attrs):
        post = attrs.get('post')
        parent = attrs.get('parent')

        # 부모 댓글이 있으면, 부모 댓글의 post와 자식 댓글의 post가 일치하는지 확인
        if parent and parent.post != post:
            raise serializers.ValidationError("The parent comment's post and the child's post don't match.")
        return attrs


class PostLikeSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source="user", read_only=True)
    post_id = serializers.PrimaryKeyRelatedField(source="follower", read_only=True)

    class Meta:
        model = PostLike
        fields = ["id", "user_id", "post_id", "created_at"]
