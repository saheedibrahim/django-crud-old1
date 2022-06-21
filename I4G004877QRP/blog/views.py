from audioop import reverse
from dataclasses import fields
import genericpath
from pyexpat import model
# from typing import Generic
from django.shortcuts import render

from I4G004877QRP.blog.models import Post

# Create your views here.
class PostListView(Generic.ListView):
    model = Post

class PostCreateView(Generic.CreateView):
    model = Post
    fields = "--all--"
    success_url = reverse_lazy("blog:all")

class PostDetailView(Generic.DetailView):
    model = Post

class PostUpdateView(Generic.UpdateView)
