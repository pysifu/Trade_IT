from django.views import generic
from django.views.generic import edit
from posts.models import Post
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin)
from django.urls import reverse_lazy
from django.shortcuts import render

from posts.mixins import GroupRequiredMixin

# Create your views here.

#List of items approved on entire marketplace
class HomeView(generic.ListView):
    model = Post
    template_name = 'posts/home_page.html'
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(is_approved=1)
    

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

# Change forbidden 403 and others html
# Add Mixins group users staff to be able to perform actions // + CBV
class ListManagePostsView(GroupRequiredMixin, generic.ListView):
    model = Post
    group_required = ['superuser', 'staff']
    paginate_by = 10
    template_name = 'posts/panel_management/list.html'
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(is_approved=2)

  
class HistoryManagePostsView(GroupRequiredMixin, generic.ListView):
      model = Post
      group_required = ['staff', 'superuser', 'admin']
      template_name = 'posts/panel_management/history.html'
      

#change label of is_approved // to do
class EditPendingPostView(edit.UpdateView):
    model = Post
    template_name = 'posts/panel_management/pending.html'
    fields = ['is_approved']
    success_url = reverse_lazy('posts:panel_pendings')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(slug=self.object.slug)
        return context

#change it to CBV // to do
#List of items posted by user
def my_items_view(request):
    posts = Post.objects.filter(user=request.user)
    context = {
        'posts' : posts
    }
    return render(request, 'posts/user/items.html', context=context)


class UserPendingItemsView(LoginRequiredMixin, generic.ListView):
    model = Post
    paginate_by = 10
    template_name = 'posts/user/pending_items.html'
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(is_approved=2)


class UserItemsView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = 'posts/user/items.html'
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(is_approved=1)


class EditUserItemView(LoginRequiredMixin, edit.UpdateView):
    model = Post
    template_name = 'posts/user/edit_item.html'
    fields = ['name', 'price', 'category', 'image']
    