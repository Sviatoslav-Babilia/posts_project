from django.db import models
from .models import User, Post
from .forms import PostChangeForm
from django.views.generic import DetailView, TemplateView, CreateView, ListView
from django.db.models import Subquery, Prefetch

# Create your views here.
class UserView(DetailView):
    template_name = 'userpage.html'
    model = User
    context_object_name = 'user'

    # def get_queryset(self, *args, **kwargs):
    #     queryset = Post.objects.all().order_by('title')
    #     # import pdb;
    #     # pdb.set_trace()
    #     return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        # following = User.objects.get(pk=pk).followers.all()
        
        followers_posts = Post.objects.filter(author__in=Subquery(self.object.followers.all().values('id'))).select_related('author')    
        context['posts'] = Post.objects.all().filter(author=pk).order_by('title')
        # context['followers'] = following
        
        
        # for us in following:
        #     voc[us.id] = []

        # for post in followers_posts:
        #     voc[post.author.id].append(post)
        # voc = {}
        # for us in following:
        #     voc[us.id] = {'user': us, 'posts': 2 }


            
        following_posts = {}
        for post in followers_posts:
            author = post.author
            if author.id in following_posts:
                if 'posts' in following_posts[author.id]:
                    following_posts[author.id]['posts'].append(post)
                else:
                    following_posts[author.id]['posts'] = [post]
            else:
                    following_posts[author.id] = {'user': author, 'posts': [post]}       
    

        context['followersposts'] = following_posts.values()  

        # foll= User.objects.get(pk=pk).followers.all().prefetch_related('followers__posts')
        

        # context['foll'] = foll
        
        # import pdb;
        # pdb.set_trace()
        return context


class AllPostsView(ListView):
    template_name = "allposts.html"

    def get_queryset(self):
        queryset = Post.objects.all().order_by('title')
        # import pdb;
        # pdb.set_trace()
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.get_queryset()

        return context
    



class PostCreateView(CreateView):
    template_name = 'post_create.html'
    form_class = PostChangeForm


class ThanksView(TemplateView):
    template_name = 'thanks.html'


