from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import UserTask
from django.urls import reverse_lazy

class Register(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('task_list')
    
    # save the form and login the user.
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)
    
    # If user is authenticated, restrict him from accessing Register page.
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task_list')
        return super(Register, self).get(*args, **kwargs)
        
    

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
        context['count'] = context['tasklist'].filter(is_completed=False).count()
        
        # Search Functionality in tasks list
        search_tasks = self.request.GET.get('search_tasks')
        if search_tasks:
            context['tasklist'] = context['tasklist'].filter(task__icontains=search_tasks)
            context['search_tasks'] = search_tasks
        return context
    
    
    
class TaskDetail(LoginRequiredMixin, DetailView):
    model = UserTask
    template_name = 'task_detail.html'
    context_object_name = 'taskdetail'
    # default name for object is object, we override the name by using context_object_name attribute.
    
    
    
class CreateTask(LoginRequiredMixin, CreateView):
    model = UserTask
    fields = ['task', 'description', 'is_completed']
    template_name = 'create_task.html'
    success_url = reverse_lazy('task_list')
    
    # setting user to request.user by overriding form_valid method
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTask, self).form_valid(form)
    
    
class UpdateTask(LoginRequiredMixin, UpdateView):
    model = UserTask
    fields = ['task', 'description', 'is_completed']
    template_name = 'create_task.html'
    success_url = reverse_lazy('task_list')
    
class DeleteTask(LoginRequiredMixin, DeleteView):
    model = UserTask
    context_object_name = 'task'
    template_name = 'delete_task.html'
    success_url = reverse_lazy('task_list')
    
    
    
    
    


