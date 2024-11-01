from django.urls import reverse_lazy
from django.views.generic import edit
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import LoginView,LogoutView
from users.forms import CustomUserCreationForm
from users.models import User
# Create your views here.

class CreateUserView(edit.FormView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('posts:home')
    
    #Zapisz konto // bez tego nie pozwala wykonac zapisu w bazie
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

class ProfileView(generic.DetailView):
    model = User
    template_name = 'users/profile.html'
    
    def get_object(self, queryset = ...):
        return get_object_or_404(User, username=self.kwargs.get('username'))


class LoginUserView(LoginView):
    template_name = 'users/login.html'
    next_page = reverse_lazy('posts:home')
    

class LogoutUserView(LogoutView):
    next_page = reverse_lazy('posts:home')
    