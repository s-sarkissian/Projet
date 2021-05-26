import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Community, Post, Comment
from .forms import PostForm, CommentForm
from django.utils import timezone

# Create your views here.
@login_required
def communautes(request):
    communautes = Community.objects.all()
    return render(request, 'communitymanager/communautes.html', {'communautes': communautes})


def login_successful(request):
    return communautes(request)


def communaute(request, id):
    posts = Post.objects.filter(community=id)
    community = Community.objects.get(id=id)
    return render(request, 'communitymanager/communaute.html', {'community': community, 'posts': posts})


def post(request, id):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=id)
    form = CommentForm(request.POST or None)
    form.post = post
    form.date_creation = timezone
    if form.is_valid():
        form.save()
        return redirect(request, post)
    return render(request, 'communitymanager/post.html', {'post': post, 'comments': comments}, locals())


def create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(request, post)
    return render(request, 'communitymanager/create.html', locals())


def feed(request):
    posts = Post.objects.order_by('-date_creation')
    return render(request, 'communitymanager/news.html', {'posts': posts})
