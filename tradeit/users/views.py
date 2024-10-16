from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from users.forms import CustomUserCreationForm

# Create your views here.


class CreateUserView(FormView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('posts:home')
    
    def form_valid(self, form):
        print('form', form.cleaned_data)
        form.save()
        return super().form_valid(form)
    
    