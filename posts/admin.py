from django.contrib import admin

from posts.models import Subreddit, Post
admin.site.register(Subreddit)
admin.site.register(Post)
