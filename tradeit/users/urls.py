from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('sign_up/', views.CreateUserView.as_view(), name='sign_up'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('profile/<slug:username>/', views.ProfileView.as_view(), name='profile'),
    
]
