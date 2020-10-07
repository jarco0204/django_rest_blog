# Django REST API Blogs

## Cross Origin Resource Sharing (CORS)

This allows your client-side application to connect with your RESTful API

1. install CORS
   - `python3 -m pip install django-cors-headers`
   - make sure it is installed `pip list`
2. Go to your project's `settings.py`
3. Under `INSTALLED_APPS` add `corsheaders`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'blog_api_app',
    'corsheaders',
]
```

4. Go to `MIDDLEWARE` and add the CORS middleware `'corsheaders.middleware.CorsMiddleware'`

```python
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

```

<b>Make sure that the middleware is at the top of the `MIDDLEWARE` or else Django will not be able to ad the CORS headers to the responses </b>

5. Configure Your Origin Path
   - add the URL of your client-side server
     - Example: React.js

```python
CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000'
]
```

Make sure your url path does not have a `/` at the end for example http://localhost:3000/ will not work as the error will read as:

```red
ERRORS:
?: (corsheaders.E014) Origin 'http://localhost:3000/' in CORS_ORIGIN_WHITELIST should not have path
```

## Nested Models

We want the client to receive API calls that allow for a nest model and can receive all the information from a single API call. <br  /> <br  />

For example, just as Twitter, you want to go a person's profile and view all their information and their recent posts. This can be done with a single API call and will be done with an api endpoint.

1. Create your models and understand what you want.
   - we want a single user to have multiple posts and those posts to have multiple replies
     - These are one-to-many relationships
2. The models must contain a `ForeignKey` with the model it has a relationship with and contain a `related_name` field
   - Here is the whole `models.py` file for the relation of
     - USER has many POSTS which has many REPLIES

```python
from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    user_image = models.URLField(null=True)

    def __str__(self):
        return self.username


class BlogPost(models.Model):
    user = models.ForeignKey(
        User, null=True, related_name='posts', on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    likes = models.PositiveIntegerField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Reply(models.Model):
    post = models.ForeignKey(
        BlogPost, related_name="replies", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
```

3. These `related_names=` properties will be used in the serializers
   - the `serializers.py` file:

```python
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
```

<b>Notice that the replies field in BlogPostSerializer is the same as related_name in the Reply Model and likewise in the UserSerializer </b>
Once those implemented the user url endpoint should look as: <br  />

![Nested!](https://i.imgur.com/TI9tKH6.png "Nested Model")
