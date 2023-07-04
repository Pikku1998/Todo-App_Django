from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserTask
from django.urls import reverse_lazy


class Login(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('task_list')


class TaskList(LoginRequiredMixin, ListView):
    model = UserTask
    template_name = 'task_list.html'
    context_object_name = 'tasklist'
    # default name for object is object_list, we override the name by using context_object_name attribute.
    
    # By default, context['tasklist'] has all the items/rows of the db. We override this method to get data related to the user only.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasklist'] = context['tasklist'].filter(user=self.request.user)
        return context
    
    
    
class TaskDetail(LoginRequiredMixin, DetailView):
    model = UserTask
    template_name = 'task_detail.html'
    context_object_name = 'taskdetail'
    # default name for object is object, we override the name by using context_object_name attribute.
    
    
    
class CreateTask(LoginRequiredMixin, CreateView):
    model = UserTask
    fields = '__all__'
    template_name = 'create_task.html'
    success_url = reverse_lazy('task_list')
    
class UpdateTask(LoginRequiredMixin, UpdateView):
    model = UserTask
    fields = '__all__'
    template_name = 'create_task.html'
    success_url = reverse_lazy('task_list')
    
class DeleteTask(LoginRequiredMixin, DeleteView):
    model = UserTask
    context_object_name = 'task'
    template_name = 'delete_task.html'
    success_url = reverse_lazy('task_list')
    
    
    
    
    


