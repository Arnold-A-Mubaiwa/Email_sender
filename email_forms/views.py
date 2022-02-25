from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            
            return HttpResponse('Thanks')
    else:
        form = NameForm()
            
    return render(request, 'forms/index.html', {'form':form})