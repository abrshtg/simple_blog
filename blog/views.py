from django.shortcuts import render, redirect, get_object_or_404
from .models import WildLife
from django.contrib import messages
from django.contrib.auth.models import User, auth
import datetime

def home(request):
    global wildlife
    wildlife = WildLife.objects.all()  # SELECT * FROM  article
    return render(request, 'blog/home.html', {'wildlife': wildlife})


def post(request):
    if request.method == 'POST':
        name = request.POST['names']
        image = request.POST['image']
        article = request.POST['article']
        author = request.POST['author']
        date = datetime.datetime.now()
        wild = WildLife.objects.create(title=name, img=image, pub_date=date, article=article, author=author)
        wild.save()
        return redirect('home')
    return render(request, 'blog/post.html')


def contact(request):
    return render(request, 'blog/contact.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('login')
        else:
            messages.info(request, 'wrong password')
            return redirect('register')
    return render(request, 'blog/register.html')


def login(request):
    home(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request, 'invalid credential')
            return redirect('login')
    return render(request, 'blog/login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


def about(request):
    return render(request, 'blog/about.html')


def detail(request, wildlife_id):
    wild = get_object_or_404(WildLife, pk=wildlife_id)
    return render(request, 'blog/detail.html', {'wild': wild})
