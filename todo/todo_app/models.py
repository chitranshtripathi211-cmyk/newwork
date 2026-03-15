from django.db import models

# Create your models here. we write here the structure of our database
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(max_length=200)
    deadline = models.DateTimeField(max_length=200)

    def __str__(self):
        return self.title