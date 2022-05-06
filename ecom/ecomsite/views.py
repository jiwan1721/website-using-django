from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'ecomsite/index.html')

def about(request):
    return HttpResponse("hi")

def analyze(request):
    text = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    uppercase = request.POST.get('uppercase','off')
   
    if removepunc=="on":
        punctuations= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''  
        analyzed = ""
        for word in text:
            if word not in punctuations:
                analyzed= analyzed + word
        context = {
            'purpose':'removing punctuations',
            'analyzed_text': analyzed}
        return render(request, 'ecomsite/analyze.html',context)
    if uppercase =="on":
        analyzed = ""
        for word in text:
            analyzed = analyzed + word.upper()
        context = {
            'purpose':'removing punctuations',
            'analyzed_text': analyzed}
        return render(request, 'ecomsite/analyze.html',context)    
    else:
        return HttpResponse('Error')
def removepunc(request):
    text = request.POST.get('text','default')
    print(text)
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("capitalize first")


def spaceremove(request):
    return HttpResponse("space remover")

def charcount(request):
    return HttpResponse("charcount ")

















def excrise1(request):
    s = ''' Navigation bar<br>'''