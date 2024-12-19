from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(verbose_name="имя", max_length=20, blank=True)
    avatar = models.FileField(verbose_name="аватар", upload_to='avatars/', blank=True)
    info = models.TextField(verbose_name="описание", max_length=100, blank=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(verbose_name="заголовок", max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="автор")
    text = models.TextField(max_length=100)
    posted_at = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    text = models.TextField('комментарий', max_length=200)
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.text
