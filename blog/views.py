from django.shortcuts import render, redirect, get_object_or_404
from blog.models import BlogPost
from blog.forms import CreateBlogPostForm, CommentForm
from django.contrib.auth.models import User


def create_blog_view(request):

    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = CreateBlogPostForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = User.objects.get(pk=user.id)
        obj.author = author
        obj.save()
        form = CreateBlogPostForm()

        context['form'] = form
    # TODO notifying about text size >
    # TODO handling not unique post titles
    return render(request, "create_blog.html", context)


def detail_blog_view(request, slug):
    context = {}

    blog_post = get_object_or_404(BlogPost, slug=slug)
    context['blog_post'] = blog_post

    return render(request, 'detail_blog.html', context)


def add_comment_to_blog(request, slug):
    context = {}

    blog_post = get_object_or_404(BlogPost, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = blog_post
            comment.save()

            context['blog_post'] = blog_post
            return redirect('../', context)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_blog.html', {'form': form})


def upvote(request, slug):
    context = {}

    blog_post = get_object_or_404(BlogPost, slug=slug)
