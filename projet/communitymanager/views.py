from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Community, Post, Comment
from .forms import PostForm, CommentForm


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
    if form.is_valid():
        form.save()
        return redirect(request, post)
    return render(request, 'communitymanager/post.html', {'post': post, 'comments': comments})


def create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(request, post)
    return render(request, 'communitymanager/create.html', locals())
