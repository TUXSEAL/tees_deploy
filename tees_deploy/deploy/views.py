from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("INDEX")

def update(request):
    return HttpResponse("UPDATE")
