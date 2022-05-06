from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'    

class PostListView(ListView):
    template_name = 'list.html'
    model = Post
    ### context_object_name = "my_list"  changes a name somewhere

class PostDetailView(DetailView):
    template_name = 'detail.html'
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'new.html'
    model = Post
    fields = ['title', 'author','body']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name= 'edit.html'
    model = Post
    fields = ['title', 'body']

class PostDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'delete.html'
    model = Post
    success_url = reverse_lazy('post_list')
##