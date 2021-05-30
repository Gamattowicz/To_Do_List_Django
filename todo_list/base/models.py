from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField


class Category(models.Model):
    name = models.CharField(max_length=200)
    color = ColorField(default='#FF0000')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{str(self.name)}'


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='task_category', null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{str(self.title)}'

    class Meta:
        ordering = ['complete']
