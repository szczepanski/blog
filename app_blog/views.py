from django.shortcuts import render, get_object_or_404
from .models import Post

def all_posts(request):
    counter_posts = Post.objects.count
    # order by most recent and limit to last 10 posts
    # delete <[:10]> to show alll posts
    posts = Post.objects.order_by('-date')[:10]
    
    # order by most recent and limit to last 5 post, here next blog functionality would have to be added
    # posts = Post.objects.order_by('-date')[:5]
    
    return render(request, 'app_blog_all_posts/all_posts.html', {'posts':posts, 'counter_posts': counter_posts })

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'app_blog_post/detail.html',{'post':post})