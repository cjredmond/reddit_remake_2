from django.conf.urls import url, include
from django.contrib import admin
from user_auth.views import UserCreateView
from posts.views import IndexView, SubredditListView, PostCreateView, SubredditDetailView, \
                        PostDetailView, PostVoteView
from comments.views import CommentCreateView, CommentVoteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include("django.contrib.auth.urls")),
    url(r'^create/user$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^subreddits/$', SubredditListView.as_view(), name="subreddit_list_view"),
    url(r'^subreddit/(?P<pk>\d+)/$', SubredditDetailView.as_view(), name="subreddit_detail_view"),
    url(r'^subreddit/(?P<pk>\d+)/post/create/$', PostCreateView.as_view(), name='post_create_view'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail_view'),
    url(r'^post/(?P<pk>\d+)/upvote/$', PostVoteView.as_view(), name='post_upvote_view'),
    url(r'^post/(?P<pk>\d+)/downvote/$', PostVoteView.as_view(), name='post_downvote_view'),
    url(r'^post/(?P<pk>\d+)/comment/$', CommentCreateView.as_view(), name='comment_create_view'),
    url(r'^comment/(?P<pk>\d+)/upvote/$', CommentVoteView.as_view(), name='comment_upvote_view'),
    url(r'^comment/(?P<pk>\d+)/downvote/$', CommentVoteView.as_view(), name='comment_downvote_view'),
]
