from django.shortcuts import render
from .models import Post # если вы выводите посты

def post_list(request):
    # Достаем все посты из базы данных
    posts = Post.objects.all()
    # Передаем их в шаблон под именем 'posts'
    return render(request, 'blog/post_list.html', {'posts': posts})