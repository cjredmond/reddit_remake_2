from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from posts.models import Subreddit, Post
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
