from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    if (removepunc=="on"):
        punctations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed=""
        for char in djtext:
            if char not in punctations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif (fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Changed to UPPER', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char!="\n":
                analyzed = analyzed + char.upper()
        params = {'purpose': 'New line removed', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed=analyzed+char
        params = {'purpose': 'Extra space removed', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Not No nope")