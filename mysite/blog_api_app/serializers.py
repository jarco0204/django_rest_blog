from rest_framework import serializers
from .models import User, BlogPost, Reply


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'


class BlogPostSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(read_only=True, many=True)

    class Meta:
        model = BlogPost
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    posts = BlogPostSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = '__all__'
