from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("<h1>Главная страница</h1><p>Переходите на /data/ или /test/</p>")


def data_page(request):
    return HttpResponse("<h1>Data Page Content</h1><p>This is the data page.</p>")

def test_page(request):
    return HttpResponse("<h1>Test Page Content</h1><p>This is the test page.</p>")

