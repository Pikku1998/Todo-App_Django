from django.urls import path
from .views import TaskList, TaskDetail, CreateTask, UpdateTask, DeleteTask, Login

urlpatterns = [
    path('', TaskList.as_view(), name='task_list'),
    path('login', Login.as_view(), name='login'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task_detail'),
    path('create-task', CreateTask.as_view(), name='create_task'),
    path('update-task/<int:pk>', UpdateTask.as_view(), name='update_task'),
    path('delete-task/<int:pk>', DeleteTask.as_view(), name='delete_task'),
      
]