from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home_page'),
    path('add_task/', add_task, name='add_task'),
    path('completed/', completed_tasks, name='completed_tasks'),
    path('remaining/', remaining_tasks, name='remaining_tasks'),
    path('task_detail/<int:pk>/', task_detail, name='task_detail'),
    path('toggle_complete/<int:pk>/', toggle_complete, name='toggle_complete'),
    path('delete_conf/<int:pk>/', delete_confirm, name='delete_confirm'),
    path('delete_task/<int:pk>/', delete_task, name='delete_task'),

]
