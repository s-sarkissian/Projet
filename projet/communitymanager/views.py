from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
def communaute(request):
    @login_required()
    return render(request, 'communitymanager/communautes.html')
