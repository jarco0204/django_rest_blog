from django.shortcuts import render
from .models import User, BlogPost
from .serializers import UserSerializer, BlogPostSerializerPOST, BlogPostSerializerGET
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.


@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def post_list_get(request):
    if request.method == "GET":
        posts = BlogPost.objects.all()
        serializer = BlogPostSerializerGET(posts, many=True)
        return Response(serializer.data)


@api_view(['POST', 'DELETE'])
def post_list_post(request):
    if request.method == "POST":
        serializer = BlogPostSerializerPOST(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        posts = BlogPost.objects.all()
        posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
