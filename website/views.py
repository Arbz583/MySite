from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
def http_test(request):
    return HttpResponse('<h2>Hi<h2>')

def json_test(request):
    return JsonResponse({'Ali':'Bakhi'})
