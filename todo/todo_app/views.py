from django.shortcuts import render

# Create your views here. w   e write here logic  our application
def home(request):
    return render(request, 'home.html')
