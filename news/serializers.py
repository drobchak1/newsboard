from rest_framework import serializers
from .models import Post, Upvote


class PostSerializer(serializers.ModelSerializer):
    upvotes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # is_fan = serializers.SerializerMethodField()
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Post
        fields = '__all__'


class UpvoteSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Upvote
        fields = '__all__'