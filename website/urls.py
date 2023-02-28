from django.urls import path
from website.views import *
urlpatterns = [
    path('',index_view),
    path('http-test',http_test),
    path('json-test',json_test),
    path('Reza',my)
    ]