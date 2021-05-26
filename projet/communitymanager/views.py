import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Community, Post, Comment
from .forms import PostForm, CommentForm
from django.utils import timezone


# Create your views here.
@login_required
def communautes(request):
    # the view that displays all communities, I did not have time to implement the subscribe button
    communautes = Community.objects.all()
    return render(request, 'communitymanager/communautes.html', {'communautes': communautes})


def login_successful(request):
    # the login successful redirects to the page displaying all communities
    return communautes(request)


def communaute(request, id):
    # the view that displays the posts from a certain community
    posts = Post.objects.filter(community=id)
    community = Community.objects.get(id=id)
    return render(request, 'communitymanager/communaute.html', {'community': community, 'posts': posts})


def post(request, id):
    # I don't understand why the comment form is not displayed despite the code being the same for it
    # and the post creation form, the only difference being that the post form has its own template
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
    # this post creation lacks proper safety like assigning the author field only the current user
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(request, post)
    return render(request, 'communitymanager/create.html', locals())


def feed(request):
    # simple view to display all posts from most recent to oldest
    posts = Post.objects.order_by('-date_creation')
    return render(request, 'communitymanager/news.html', {'posts': posts})


def modify(request, id):
    # this view lacks the proper safety like not modifiable author, and title
    form = PostForm(request.POST or None)
    form.post = Post.objects.get(id=id)
    if form.is_valid():
        form.save()
    return render(request, 'communitymanager/modify.html', locals())
