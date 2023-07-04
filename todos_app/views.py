from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import UserTask
from django.urls import reverse_lazy


class TaskList(ListView):
    model = UserTask
    template_name = 'task_list.html'
    context_object_name = 'tasklist'
    
    
class TaskDetail(DetailView):
    model = UserTask
    template_name = 'task_detail.html'
    context_object_name = 'taskdetail'
    
    
class CreateTask(CreateView):
    model = UserTask
    fields = '__all__'
    template_name = 'create_task.html'
    success_url = reverse_lazy('task_list')
    
class UpdateTask(UpdateView):
    model = UserTask
    fields = '__all__'
    template_name = 'create_task.html'
    success_url = reverse_lazy('task_list')
    
class DeleteTask(DeleteView):
    model = UserTask
    context_object_name = 'task'
    template_name = 'delete_task.html'
    success_url = reverse_lazy('task_list')
    
    
    
    
    


