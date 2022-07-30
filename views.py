from asyncio.proactor_events import _ProactorDuplexPipeTransport
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html",)

def analyse(request):
    save= request.GET.get('text','default')
    removepunc= request.GET.get('analyse','off')
    print(save)
    print(removepunc)
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analysed = ""
        for char in save:
            if char not in punctuations:
                analysed = analysed + char

    params= {'purpose':'Removed Punctuations','analysed_text':analysed}
    return render (request, 'analyse.html',params) 
    

# def capfirst(request):
   # return HttpResponse("capitalize first")

# def newlineremove(request):
    #return HttpResponse("capitalize first")


# def spaceremove(request):
    #return HttpResponse("space remover")

# def charcount(request):
    #return HttpResponse("charcount ")
