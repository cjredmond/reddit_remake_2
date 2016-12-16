from django.conf.urls import url, include
from django.contrib import admin
from user_auth.views import UserCreateView
from posts.views import IndexView, SubredditListView, PostCreateView, SubredditDetailView, \
                        PostDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include("django.contrib.auth.urls")),
    url(r'^create/user$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^subreddits/$', SubredditListView.as_view(), name="subreddit_list_view"),
    url(r'^subreddit/(?P<pk>\d+)/$', SubredditDetailView.as_view(), name="subreddit_detail_view"),
    url(r'^subreddit/(?P<pk>\d+)/post/create/$', PostCreateView.as_view(), name='post_create_view'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail_view'),
]
