from django.urls import path, include
from .views import user_list, post_list_get, post_list_post

urlpatterns = [
    path('users/', user_list),
    path('blogpost_get/', post_list_get),
    path('blogpost_post/', post_list_post)
]
