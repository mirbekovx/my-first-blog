from django.contrib import admin
from django.urls import path
from blog import views  # <--- ОЧЕНЬ ВАЖНО: импортируем именно из папки blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_list, name='post_list'),
]