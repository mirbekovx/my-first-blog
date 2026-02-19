from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-created_date')
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})

def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        text = request.POST.get('text')
        if author_name and text:
            Comment.objects.create(post=post, author_name=author_name, text=text)
            return redirect('post_detail', pk=pk)
    return redirect('post_detail', pk=pk)
