from django.contrib import admin
from django.urls import path,include
from.import views
urlpatterns = [
    path('',views.index, name='index'),
    path('update/<str:pk>/',views.update, name='update'),
    path('delete/<str:pk>/',views.delete, name='delete'),
    path('api-auth/',views.api,name='api'),
    path('task-list/',views.tasklist,name='task-list'),
    path('task-detail/<str:pk>',views.taskdetail,name='task-detail'),
    path('task-create/',views.taskcreate,name='task-create'),
    path('task-update/<str:pk>',views.taskupdate,name='task-update'),
    path('task-delete/<str:pk>',views.taskdelete,name='task-delete'),
    ]