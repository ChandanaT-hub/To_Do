from django.shortcuts import render,redirect
from django.http import JsonResponse
from.models import *
from.forms import *
from.serializers import TaskSerializer
from.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
# Create your views here.
@api_view(['GET'])
def api(request):
    api_urls= {
        'List':"/task-list/",
        'Detail View': '/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
    }

    return Response(api_urls)
@api_view(['GET'])
def tasklist(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks,many=True)

    return Response(serializer.data)
@api_view(['GET'])
def taskdetail(request,pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks,many=False)

    return Response(serializer.data)
@api_view(['POST'])
def taskcreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def taskupdate(request,pk):
    tasks=Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=tasks,data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def taskdelete(request,pk):
    tasks=Task.objects.get(id=pk)
    tasks.delete()


    return Response("ITEM DELETED SUCCESSFULLY")


def index(request):
    tasks=Task.objects.all()
    form = TaskForm()
    if request.method=="POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    content={
        'tasks':tasks,
        'form':form
    }
    return render(request,'index.html',content)

def update(request,pk):
    task=Task.objects.get(id=pk)
    form=TaskForm(instance=task)

    if request.method=='POST':
        form=TaskForm(request.POST,instance=task)

        if form.is_valid():
            form.save()
            return redirect("/")
    content = {
        'form': form
    }
    return render(request,'update.html',content)

def delete(request,pk):
    item=Task.objects.get(id=pk)

    if request.method=="POST":
        item.delete()
        return redirect("/")
    content={'item':item}
    return  render(request,'delete.html',content)


class RegisterUser(APIView):
    def post(self,request):
        serializer = UserSerializer(data = request.data)
        
        if not serializer.is_valid():
            return Response({'status':403 , 'errors':serializer.errors,'message':'some errors'})
            
            
        serializer.save()

        user = User.objects.get(username = serializer.data['username'])
        token_obj , _ = Token.objects.get_or_create(user=user)

        return Response({'status':200,'payload':serializer.data,'message':'your data is saved'})
