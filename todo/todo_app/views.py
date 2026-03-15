from django.shortcuts import render , redirect
from .models import Todo

from django.shortcuts import redirect, render
from .models import Todo

# Create your views here. we rite here logic  our application
def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        completed = request.POST.get('completed') == 'on'  # Checkbox returns 'on' when checked
        deadline = request.POST.get('deadline')
        created_at = request.POST.get('created_at')
        task = Todo(title=title, description=description, completed=completed, deadline=deadline, created_at=created_at)
        task.save()# Redirect to the home page after saving the task
        return redirect('home')
    return render(request, 'home.html')
 # Render the home page template for GET requests



def taskDisplay(request):
    task = Todo.objects.all()  # Retrieve all tasks from the database

    return render(request, 'task_display.html', {'task': task})  # Pass the tasks to the template for rendering



def deleteTask(request, id):
    task = Todo.objects.get(id=id)
    task.delete()
    return redirect('task')