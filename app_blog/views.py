from django.shortcuts import render, get_object_or_404
from .models import Post

def all_posts(request):
    # order by most recent
    posts = Post.objects.order_by('-date')
    
    # order by most recent and limit to last 5 blogs, here next blog functionality would have to be added
    # posts = Post.objects.order_by('-date')[:5]
    
    return render(request, 'app_blog_all_posts/all_posts.html', {'posts':posts})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'app_blog_post/detail.html',{'post':post})