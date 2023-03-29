from django.urls import path
from users.views import MyLogin, MyRegister

app_name = 'users'

urlpatterns = [
    path('login/', MyLogin, name='login'),
    path('register/', MyRegister, name='register'),
]
