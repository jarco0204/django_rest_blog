from django.urls import path, include
from .views import user_list, post_list, reply_list

urlpatterns = [
    path('users/', user_list),
    path('blogpost_get/', post_list),
    path('replies/', reply_list)
]
