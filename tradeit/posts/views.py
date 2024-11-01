from django.shortcuts import redirect
from django.views import generic
from django.views.generic import edit
from posts.models import Post

# Create your views here.


class HomeView(generic.ListView):
    model = Post
    template_name = 'posts/home_page.html'
    
    
class CreatePostView(edit.CreateView):
    model = Post
    template_name = 'posts/create_post.html'
    fields = ['name', 'price', 'category', 'image']
    
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)
    
    
class PostView(generic.DetailView):
    model = Post
    template_name = 'posts/post.html'
    
