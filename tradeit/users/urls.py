from django.urls import path
from users.views import CreateUserView

app_name = 'users'

urlpatterns = [
    path('sign_up/', CreateUserView.as_view(), name='sign_up'),
    
]
