from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta, timezone
from django.utils import timezone
from comments.models import Comment

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

    def vote_count(self):
        return sum([vote.score for vote in self.postvote_set.all()])

    def comment_list(self):
        return self.comment_set.all()

class PostVote(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)
    value = models.BooleanField()

    class Meta:
        unique_together = ('user', 'post')

    @property
    def score(self):
        if self.value:
            return 1
        return -1
