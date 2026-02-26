from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from django.contrib.auth.forms import UserCreationForm
from .forms import CommentForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'form': form,
    })


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_date')
    serializer_class = PostSerializer

    # Используем ТОЛЬКО этот метод для логирования
    def initial(self, request, *args, **kwargs):
        # 1. Сначала даем DRF сделать свою работу
        super().initial(request, *args, **kwargs)

        # 2. Печатаем данные (flush=True обязателен для Docker)
        print("\n" + "=" * 30, flush=True)
        print(f"METHOD: {request.method}", flush=True)
        print(f"DATA: {request.data}", flush=True)
        print("=" * 30 + "\n", flush=True)