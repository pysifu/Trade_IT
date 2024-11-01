from django.urls import path
from posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('create/post/', views.CreatePostView.as_view(), name='create_post'),
    path('post/<slug:slug>/', views.PostView.as_view(), name='post'),
]