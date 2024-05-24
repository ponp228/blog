from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Post, Category, Comment
from.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q

# Create your views here.
def index(request):
    slides = Post.objects.filter(feature = True).order_by('-created_at')[:4]
    posts = Post.objects.order_by('-created_at')[:8]
    categories = Category.objects.all()[:12]
    return render(request, 'index.html', {'posts':posts, 'slides':slides,'categories': categories })


def post_detail(request,slug):
    post = Post.objects.get(slug__exact=slug)
    return render(request, 'post_detail.html', {'post':post})

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user=form.save()
                login(request, user)
                return redirect('index')
        else:
            form = RegisterForm()
        return render(request, 'register.html', {'form':form})
    return redirect('index')
def login_site(request):
    if not request.user.is_authenticated:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html')
def logout_site(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')

def comment(request, slug):
    if request.method == 'POST':
        comment = Comment()
        comment.post = Post.objects.get(slug__exact=slug)
        comment.author = request.user
        comment.text = request.POST.get('comment')
        comment.save()
    return redirect(reverse('post_detail_url', kwargs={'slug':slug}))

def category_detail(request, slug):
    category = Category.objects.get(slug__exact=slug)
    return render(request, 'category_detail.html', {'category': category})

def search_function(request):
    query = request.GET.get('search_input')
    posts = Post.objects.filter(Q(title__iregex = query))
    return render(request, 'search.html', {'query': query, 'posts': posts})
def search(request):
    news = Post.objects.all()
    return render(request, {'news': news})