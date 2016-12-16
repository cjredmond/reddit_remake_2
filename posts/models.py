from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta, timezone
from django.utils import timezone

class Subreddit(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def post_list(self):
        return self.post_set.all()

class Post(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)
    subreddit = models.ForeignKey(Subreddit)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title
