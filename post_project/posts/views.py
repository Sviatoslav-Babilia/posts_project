from django.shortcuts import render
from .models import User, Post
from .forms import PostChangeForm
from django.views.generic import UpdateView, DeleteView, DetailView, TemplateView, FormView, CreateView, ListView

# Create your views here.
class UserView(ListView):
    template_name = 'home.html'

    def get_queryset(self, **kwargs):
        posts = Post.objects.filter(autor=self.request.user).order_by('title')


class PostCreateView(CreateView):
    template_name = 'post_create.html'
    form_class = PostChangeForm


