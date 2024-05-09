from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from .views import RegisterUser
from.import views
urlpatterns = [
    path('',views.index, name='index'),
    path('register/', TemplateView.as_view(template_name='register.html'), name='registration'),
    # path('login/',views.user_login,name='login'),
    path('update/<str:pk>/',views.update, name='update'),
    path('delete/<str:pk>/',views.delete, name='delete'),
    path('api-auth/',views.api,name='api'),
    path('register/',RegisterUser.as_view(),name='RegisterUser'),
    path('task-list/',views.tasklist,name='task-list'),
    path('task-detail/<str:pk>',views.taskdetail,name='task-detail'),
    path('task-create/',views.taskcreate,name='task-create'),
    path('task-update/<str:pk>',views.taskupdate,name='task-update'),
    path('task-delete/<str:pk>',views.taskdelete,name='task-delete'),
    ]