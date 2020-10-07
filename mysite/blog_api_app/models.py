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
