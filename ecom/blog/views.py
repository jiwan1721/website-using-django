from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def about(request):
    return HttpResponse("return about")

def contact(request):
    return HttpResponse("return contact page")

def tracker(request):
    return HttpResponse("tracker")

def checkout(request):
    return HttpResponse("tracker")
def search(request):
    return HttpResponse("tracker")
def ProductView(request):
    return HttpResponse("tracker")