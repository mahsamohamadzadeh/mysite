from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import CommentForm
from django.contrib import messages


# Create your views here.


# def blog_view(request, cat_name=None, author_username=None):
#     posts = Post.objects.filter(status=1)
#     if cat_name:
#         posts = posts.filter(category__name=cat_name)
#     if author_username:
#         posts = posts.filter(author__username=author_username)
#     context = {"posts": posts}
#     return render(request, 'blog/blog-home.html', context)

def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name'):
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username'):
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name'):
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    context = {"posts": posts}
    return render(request, 'blog/blog-home.html', context)


def blog_detail(request, pid):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'your comment save successfully', 'success')
        else:
            messages.success(request, 'your comment save successfully', 'success')

    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid)
    comments = Comment.objects.filter(post=post.id, approved=True)
    form = CommentForm()
    context = {'post': post, 'comments': comments, 'form': form}
    return render(request, 'blog/blog-single.html', context)


def test(request):
    # posts = Post.objects.all()
    # posts = Post.objects.filter(status=1)
    # post = get_object_or_404(Post, pk=pid)
    # context = {"post": post}
    return render(request, 'test.html')


def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {"posts": posts}
    return render(request, 'blog/blog-home.html', context)


def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)

    context = {"posts": posts}
    return render(request, 'blog/blog-home.html', context)
