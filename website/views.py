from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
def http_test(request):
    return HttpResponse('<h2>Hi<h2>')

def json_test(request):
    return JsonResponse({'Ali':'Bakhi'})

def index_view(request):
    return(render(request,'index.html'))

def my(request):
    return(render(request,'oh/my.html'))

