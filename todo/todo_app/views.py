from django.shortcuts import render

# Create your views here. we write here log of our application
def home(request):
    return render(request, 'home.html')
