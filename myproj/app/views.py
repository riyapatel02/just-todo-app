from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import *

# Create your views here.
def home(request):
    context= {}
    #sendind data from frontend to backend
    if request.method == 'POST':
        todo = request.POST.get('todo')

        todo_obj = Todo.objects.create(todo_name=todo)
        return redirect('/')

    
    #to fetch data from backend-->
    context['todos'] = Todo.objects.all() 

    return render(request, 'home.html',context)

# --->DELETE FUNC OF todo--->
def delete_todo(request, id):
    try:
        todo_obj = Todo.objects.get(id=id).delete()
    except Exception as e:
        print(e)

    return redirect('/')

#---->Update Funcn --->
def update_todo(request):
    id = request.GET.get('id')
    try:
        todo_obj = Todo.objects.get(id=id)
        todo_iscompleted = not todo_obj.is_completed
        todo_obj.save()
    except Exception as e:
        print(e)

    return redirect('/')

def login(request):
    if request.method =='POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            return redirect('/login/')

        user_obj = authenticate(username=username,password=password)

        if user_obj:
            login(request,user_obj)
            return redirect('/')
        messages.error(request,'please enter correct credentials')
        return redirect('/login/')

    return render(request,'login.html')

def register(request):
    if request.method =='POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return redirect('/login/')

        user_obj = User(username=username,password=password)
        user_obj.set_password(password)
        user_obj.save()
        messages.info(request,"you have been Registerd!")
        return redirect('/login/')
    return render(request,'register.html')

def logout(request):
    logout(request)
    return redirect('/login/')