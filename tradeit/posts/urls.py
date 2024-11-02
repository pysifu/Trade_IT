from django.urls import path
from posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('create/post/', views.CreatePostView.as_view(), name='create_post'),
    path('post/<slug:slug>/', views.PostView.as_view(), name='post'),
    path('my_posts/items/', views.my_items_view, name='items'),
    path('manage/items/pending/', views.ManagePostsView.as_view(), name='pending_items'),
]