from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'    

class PostListView(ListView):
    template_name = 'list.html'
    model = Post

class PostDetailView(DetailView):
    template_name = 'detail.html'
    model = Post

class PostCreateView(CreateView):
    template_name = 'new.html'
    model = Post
    fields = ['title', 'body', 'author']

class PostUpdateView(UpdateView):
    template_name= 'edit.html'
    model = Post
    fields = ['title', 'body']

class PostDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Post
    success_url = reverse_lazy('post_list')