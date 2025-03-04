from django.shortcuts import render, redirect
from .forms import UserInputForm
from django.http import HttpResponse
# Create your views here.
def api(request):
    return HttpResponse("<h1>Main</h1>")

def about(request):
    return HttpResponse("<h1>About</h1>")