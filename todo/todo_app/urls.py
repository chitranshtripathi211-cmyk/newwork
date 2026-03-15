from django.urls import path 
from .views import home ,taskDisplay, deleteTask


urlpatterns = [path('', home, name='home'),
        path('task', taskDisplay, name='task'),
        path('delete/<int:id>', deleteTask, name='taskDelete')
]