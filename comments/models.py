from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta, timezone
from django.utils import timezone

class Comment(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey('posts.Post')
    body = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)

    @property
    def vote_count(self):
        return sum([vote.score for vote in self.commentvote_set.all()])

class CommentVote(models.Model):
    user = models.ForeignKey(User)
    comment = models.ForeignKey(Comment)
    value = models.BooleanField()

    class Meta:
        unique_together = ('user', 'comment')

    @property
    def score(self):
        if self.value:
            return 1
        return -1
