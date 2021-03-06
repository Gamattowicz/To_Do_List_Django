from django import forms
from .models import Task, Category
from django.forms.widgets import TextInput, DateInput


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content', 'complete', 'deadline', 'category']
        title = forms.CharField(label='Title', max_length=200)
        widgets = {
            'deadline': DateInput(attrs={'type': 'date'})
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'color']
        widgets = {
            'color': TextInput(attrs={'type': 'color'})
        }