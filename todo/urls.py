from django.urls import path
from todo.views import index, update, delete

app_name = 'index'

urlpatterns = [
    path('', index, name='index'),
    path('update/', update, name='update'),
    path('delete/', delete, name='delete'),
]
