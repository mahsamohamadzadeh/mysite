from django import template
from blog.models import Post, Category,Comment

register = template.Library()


@register.simple_tag
def hello():
    return 'hello'


@register.simple_tag(name='totalposts')
def function():
    # posts = Post.objects.filter(status=1).count()
    posts = Post.objects.filter(status=1)
    return posts

@register.simple_tag(name='comments_count')
def function(pid):
    post = Post.objects.get(pk=pid)
    return Comment.objects.filter(post=post.id,approved=True).count()

@register.filter
def snippet(value, args):
    return value[:args] + '...'


@register.inclusion_tag('blog/blog-popular-posts.html')
def latestpost(args=3):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:args]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories': cat_dict}
