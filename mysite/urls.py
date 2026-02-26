from django.contrib import admin
from django.urls import path, include
from blog import views
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from blog.views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet) # Теперь эндпоинт будет /posts/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('register/', views.register, name='register'),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='blog/login.html'),
        name='login',
    ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
]