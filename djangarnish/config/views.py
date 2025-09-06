from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    '''
    Home page
    '''
    return render(request, 'home.html')


def favicon_view(request):
    '''
    Stop annoying logging/messages about favicon
    '''
    return HttpResponse(status=204)  # No Content
