from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    template = 'posts/index.html'
    return render(request, template)
    # Create your views here.    
def group_posts(request, pk):
    return HttpResponse('Групповой пост<slug>')