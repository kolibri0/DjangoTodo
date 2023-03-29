from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='login')),
    path('', include('todo.urls', namespace='index'))
]
