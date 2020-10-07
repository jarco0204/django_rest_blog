from rest_framework import serializers
from .models import User, BlogPost


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BlogPostSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'

# IN ORDER TO SEE ALL OF THE POSTS, WITH DEPTH 1, YOU NEED TO MAKE A NEW SERIALIZER


class BlogPostSerializerGET(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
        depth = 1
