from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def page1(request):
    return render(request, 'page1.html')
def page2(request):
    ip = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
    user_info = request.META.get('Http_USER_AGENT')
    return render(request, 'page2.html',locals())
