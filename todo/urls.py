from django.urls import path
from todo.views import index

app_name = 'index'

urlpatterns = [
    path('', index, name='index'),
]
