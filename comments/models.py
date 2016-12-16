from django.db import models
from posts.models import Post
from django.contrib.auth.models import User
from datetime import datetime, timedelta, timezone
from django.utils import timezone

class Comment(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    body = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
