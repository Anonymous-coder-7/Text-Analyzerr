# this one is created by me
from django.http import HttpResponse     # this is imported by me
from django.shortcuts import render      # this is imported by me


def index(request):                       # the function which we want the site to do
    return render(request,'index.html')

def analyze(request):
    djangotext=request.POST.get('text','default')  #takes the value whose name is text else gives default value
    checkpunctuation=request.POST.get('removepunctuation','off')
    checkcapital=request.POST.get('capitalize','off')
    checknewline=request.POST.get('newlineremover','off')
    
    if(checkpunctuation=='on'):
        analyzed=""
        punctuations=''' ()[]{}\|?/<>!@#$%&*_ " ' , . : ; ^ '''
        for char in djangotext:
            if char not in punctuations:
                analyzed+=char
        params={'purpose':'remove punctuations','analyzedtext':analyzed}
        djangotext=analyzed
    if(checkcapital=='on'):
        analyzed=""
        for char in djangotext:
            analyzed+=char.upper()
        params={'purpose':'capitalize','analyzedtext':analyzed}
        djangotext=analyzed
    if(checknewline=='on'):
        analyzed=""
        for char in djangotext:
            if(char!='\n'):
                analyzed+=char
        params={'purpose':'new line removed','analyzedtext':analyzed}
        djangotext=analyzed
    if(checkpunctuation !='on' and checkcapital!='on' and checknewline!='on'):
        return HttpResponse("error")
    
    return render(request,'analyze.html',params)
    


