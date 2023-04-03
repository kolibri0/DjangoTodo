from django.urls import path
from todo.views import index, update, delete, create

app_name = 'index'

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
]
