from django.urls import path
from . import views
from .feeds import LatestEntriesFeed

app_name = 'blog'

urlpatterns = [
    path('', views.blog_view, name='index'),
    path('<int:pid>/', views.blog_detail, name='detail'),
    path('category/<str:cat_name>/', views.blog_view, name='category'),
    path('tag/<str:tag_name>/', views.blog_view, name='tag'),
    path('author/<str:author_username>/', views.blog_view, name='author'),
    path('search/', views.blog_search, name='search'),
    path('rss/feed/', LatestEntriesFeed()),

    # path('test-<int:pid>/', views.test),
    # path('test/', views.test),


]
