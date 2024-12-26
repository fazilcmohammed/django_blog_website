from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Post
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    if request.user.is_authenticated: 
        full_name = f"{request.user.first_name} {request.user.last_name}" 
    else: 
        full_name = None

    articles = Post.objects.all()
    featured_posts = Post.objects.order_by('priority')[:4]

    return render(request, 'home.html', {'full_name' : full_name, "articles" : articles, "featured":featured_posts})

@login_required
def newpost(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        category_id = request.POST['category']
        category = Category.objects.get(id=category_id)
        image = request.FILES.get('image')

        post = Post.objects.create(
            title=title,
            content = content,
            author = request.user,
            category = category,
            image = image
            )
        return redirect('createdpost', id=post.id)
    categories = Category.objects.all()
    return render(request, 'new_post.html', {'categories':categories})

def createdpost(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'created_post.html', {'post':post})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    posts = Post.objects.filter(author=request.user, delete_status=Post.LIVE)
    
    return render(request, 'post_detail.html', {'post': post, 'posts':posts})