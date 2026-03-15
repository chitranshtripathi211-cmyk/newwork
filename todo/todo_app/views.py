from django.shortcuts import render

# Create your views here. we rite here logic  our application
def home(request):
    return render(request, 'home.html')
