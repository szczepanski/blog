from django.shortcuts import render, get_object_or_404
from .models import Post

def all_posts(request):
    # order by most recent
    posts = Post.objects.order_by('-date')
    
    # order by most recent and limit to last 5 blogs, here next blog functionality would have to be added
    # posts = Post.objects.order_by('-date')[:5]
    
    return render(request, 'app_blog_all_posts/all_posts.html', {'posts':posts})

# def detail(request, blog_id):
#     blog = get_object_or_404(Blog, pk=blog_id)
#     return render(request, 'blog/detail.html',{'blog':blog})