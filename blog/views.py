from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class DetailListView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class BlogUdateView(UpdateView):
    model = Post
    fields = ['title','body']
    template_name = 'post_edit.html'    

class DEletedBlogView(DeleteView):
    model = Post
    template_name = 'delete.html'    
    success_url = reverse_lazy('home')


