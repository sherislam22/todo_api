from email.policy import default
from unicodedata import category
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class TodoList(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    creates = models.DateField(default=timezone.now().strftime("%Y=%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y=%m-%d"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    
    
    def __str__(self):
        return self.title

