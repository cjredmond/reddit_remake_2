from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from posts.models import Post
from comments.models import Comment, CommentVote
from django.urls import reverse, reverse_lazy

class CommentCreateView(CreateView):
    model = Comment
    fields = ('body',)
    def get_success_url(self, **kwargs):
        target = Post.objects.get(id=self.kwargs['pk'])
        return reverse_lazy('post_detail_view', args=str(target.id,))

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.post = Post.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

class CommentVoteView(CreateView):
    model = CommentVote
    fields = ('value',)
    def get_success_url(self, **kwargs):
        target = Comment.objects.get(id=self.kwargs['pk'])
        return reverse_lazy('post_detail_view', args=str(target.post.id,))
    def form_valid(self, form):
        try:
            CommentVote.objects.get(user=self.request.user, comment_id=self.kwargs['pk']).delete()
        except CommentVote.DoesNotExist:
            pass
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.comment = Comment.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)
