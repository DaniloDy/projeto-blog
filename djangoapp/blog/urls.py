from blog.views import category, created_by, index, page, post, search, tag
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('post/<slug:slug>/', post, name='post'),
    path('page/<slug:slug>/', page, name='page'),
    path('created_by/<int:author_pk>/', created_by, name='created_by'),
    path('category/<slug:slug>/', category, name='category'),
    path('tag/<slug:slug>/', tag, name='tag'),
    path('search/', search, name='search'),
]