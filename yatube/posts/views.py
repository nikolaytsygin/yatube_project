from django.http import HttpResponse

def index(request):
    return HttpResponse('Главная страница')
    # Create your views here.    
def group_posts(request, pk):
    return HttpResponse('Групповой пост<slug>')