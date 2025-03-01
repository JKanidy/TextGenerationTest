from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import UserInput
from .forms import UserInputForm

# Create your views here.
def index(request):
    if request.POST:
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request, 'TextGeneration/index.html', {'form': UserInputForm})

def about(request):
    return render(request, 'TextGeneration/about.html')