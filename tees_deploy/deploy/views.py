from django.shortcuts import render
from django.http import HttpResponse
import os

def index(request):
    return HttpResponse("INDEX")

def update(request):
    os.system("git pull origin main")
    return HttpResponse("UPDATE")
