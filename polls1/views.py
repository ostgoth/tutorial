from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Polls 1!!111")


