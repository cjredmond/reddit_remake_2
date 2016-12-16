from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from posts.models import Subreddit, Post, PostVote
from django.urls import reverse, reverse_lazy

class IndexView(TemplateView):
    template_name = "index.html"

class SubredditListView(ListView):
    model = Subreddit

class SubredditDetailView(DetailView):
    model = Subreddit

class PostCreateView(CreateView):
    model = Post
    success_url = "/"
    fields = ('title', 'body')

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.subreddit = Subreddit.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = Post

class PostVoteView(CreateView):
    model = PostVote
    fields = ('value',)
    def get_success_url(self, **kwargs):
        target = Post.objects.get(id=self.kwargs['pk'])
        return reverse_lazy('post_detail_view', args=(target.id,))
    def form_valid(self, form):
        try:
            PostVote.objects.get(user=self.request.user, post_id=self.kwargs['pk']).delete()
        except PostVote.DoesNotExist:
            pass
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.post = Post.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)
