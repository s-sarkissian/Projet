from django.shortcuts import render


# Create your views here.
def community(request):
    return render(request, 'communitymanager/communities.html')
