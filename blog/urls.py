from django.urls import path
from blog.views import (

    create_blog_view,
    detail_blog_view,
    add_comment_to_blog,
)

app_name = 'blog'

urlpatterns = [
    path('create/', create_blog_view, name='create'),
    path('<slug>/', detail_blog_view, name='detail'),
    path('<slug>/comment/', add_comment_to_blog, name='add_comment_to_blog'),
]