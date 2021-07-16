from rest_framework import serializers
from users.models import User
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    User = get_user_model()
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = "__all__"
