from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from personal.models import Question
from django.http import HttpResponse
from .models import LoginForm
from blog.models import BlogPost


def home_screen_view(request):
    context = {}
    questions = Question.objects.all()
    context["qustions"] = questions

    blog_posts = BlogPost.objects.all()
    context['blog_posts'] = blog_posts
    return render(request, "home.html", context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print('form is valid')
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                print('user is not none')
                if user.is_active:
                    print('user is active')
                    login(request, user)
                    return redirect('home')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


def must_authenticate_view(request):
    return render(request, 'must_authenticate.html', {})



