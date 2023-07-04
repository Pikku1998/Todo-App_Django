from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import UserTask


class TaskList(ListView):
    model = UserTask
    template_name = 'task_list.html'
    
    
class TaskDetail(DetailView):
    model = UserTask
    template_name = 'task_detail.html'
    
    


