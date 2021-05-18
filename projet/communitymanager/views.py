from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from models import Communaute


# Create your views here.
def communaute(request):
    @login_required()
    communautes = Communaute.object.all()
    return render(request, 'communitymanager/communautes.html', {'communautes':communautes})


def login_successful(request):
    return redirect('communitymanager/communautes.html')
