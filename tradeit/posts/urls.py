from django.urls import path
from posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('create/post/', views.CreatePostView.as_view(), name='create_post'),
    path('post/<slug:slug>/', views.PostView.as_view(), name='post'),
    path('user/items/', views.UserItemsView.as_view(), name='user_items'),
    path('user/item/edit/<slug:slug>/', views.EditUserItemView.as_view(), 
         name='user_edit_item'),
    path('user/items/pending/', views.UserPendingItemsView.as_view(), 
         name='user_pending_items'),
    path('manage/items/pending/', views.ListManagePostsView.as_view(), 
         name='panel_pendings'),
    path('manage/items/pending/<slug:slug>', views.EditPendingPostView.as_view(), 
         name='panel_edit_pending'),
    path('manage/items/history/', views.HistoryManagePostsView.as_view(), 
         name='panel_history'),
]