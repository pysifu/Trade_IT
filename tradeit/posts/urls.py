from django.urls import path
from posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('create/post/', views.PostCreateView.as_view(), name='create_post'),
    path('post/<slug:slug>/', views.PostView.as_view(), name='post'),
    path('user/posts/', views.UserPostsView.as_view(), name='user_posts'),
    path('user/post/edit/<slug:slug>/', views.UserEditPostView.as_view(), 
         name='user_edit_post'),
    path('user/posts/pending/', views.UserPendingPostsView.as_view(), 
         name='user_pending_posts'),
    path('manage/posts/pending/', views.PanelListPostsView.as_view(), 
         name='panel_pendings'),
    path('manage/posts/pending/<slug:slug>', views.PanelEditPostView.as_view(), 
         name='panel_edit_pending'),
    path('manage/posts/history/', views.PanelHistoryPostsView.as_view(), 
         name='panel_history'),
]