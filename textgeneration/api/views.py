from django.shortcuts import render, redirect
from .forms import UserInputForm

# Create your views here.
def api(request):
    if request.POST:
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('api')
    return render(request, 'textgeneration-app/public/api.html', {'form': UserInputForm})

def about(request):
    return render(request, 'textgeneration-app/public/api.html')