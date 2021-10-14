from django.shortcuts import render
from .models import User
from django.views.generic import UpdateView, DeleteView, DetailView, TemplateView, FormView, CreateView, ListView

# Create your views here.
class UserView(TemplateView):
    template_name = 'home.html'


