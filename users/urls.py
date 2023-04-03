from django.urls import path
from users.views import MyLogin, MyRegister, MyLogout

app_name = 'users'

urlpatterns = [
    path('login/', MyLogin, name='login'),
    path('register/', MyRegister, name='register'),
    path('logout/', MyLogout, name='logout'),
]
