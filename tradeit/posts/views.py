from django.views import generic
from django.views.generic import edit
from posts.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_list_or_404, render

# Create your views here.

#List of items on entire marketplace
class HomeView(generic.ListView):
    model = Post
    template_name = 'posts/home_page.html'
    

#Create item by user // only authorized users.
class CreatePostView(LoginRequiredMixin, edit.CreateView):
    model = Post
    template_name = 'posts/create_post.html'
    fields = ['name', 'price', 'category', 'image']
    login_url = reverse_lazy('users:login')
    
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)
 
    
#Detail about item
class PostView(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = 'posts/post.html'
    
# Add Mixins group users staff to be able to perform actions // + CBV
class ManagePostsView(generic.TemplateView):
    template_name = 'posts/panel_manage_posts/pending.html'

#List of items posted by user
def my_items_view(request):
    posts = Post.objects.filter(user=request.user)
    context = {
        'posts' : posts
    }
    return render(request, 'posts/my_posts/items.html', context=context)



#user sold items
def sold_items_view(request):
    pass

#pending items to approve by administrator // FBV or CBV?
def pending_items_view(request):
    pass