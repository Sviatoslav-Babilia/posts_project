from django.shortcuts import render
from .models import User, Post
from .forms import PostChangeForm
from django.views.generic import UpdateView, DeleteView, DetailView, TemplateView, FormView, CreateView, ListView

# Create your views here.
class UserView(DetailView):
    template_name = 'userpage.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Post.objects.all().order_by('title')
        # import pdb;
        # pdb.set_trace()
        return queryset


        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['posts'] = Post.objects.all().filter(author=pk).order_by('title')
        # import pdb;
        # pdb.set_trace()
        return context



class PostCreateView(CreateView):
    template_name = 'post_create.html'
    form_class = PostChangeForm


class ThanksView(TemplateView):
    template_name = 'thanks.html'


