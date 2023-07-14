from django.urls import path
from .views import TaskList, TaskDetail, CreateTask, UpdateTask, DeleteTask, Login, register_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('register', register_view, name='register'),
    path('tasks', TaskList.as_view(), name='task_list'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task_detail'),
    path('create-task', CreateTask.as_view(), name='create_task'),
    path('update-task/<int:pk>', UpdateTask.as_view(), name='update_task'),
    path('delete-task/<int:pk>', DeleteTask.as_view(), name='delete_task'),    
]