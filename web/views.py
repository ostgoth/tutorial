from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # Phase # 1: accepting data
    print ('body %s') % request.body
    print ('GET %s') % request.GET
    print ('POST %s') % request.POST
    # Phase # 2: Sending data
    return HttpResponse('{HelloJSON:2}', content_type="application/json")