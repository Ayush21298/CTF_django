from django.shortcuts import render

# Create your views here.

def user_list(request):
    return render(request,'user/user_list.html',{})

def index(request):
    return render(request,'user/index.html',{})

def login(request):
    return render(request,'user/login.html',{})

def signup(request):
    return render(request,'user/signup.html',{})

def contest(request):
    return render(request,'user/contest.html',{})

def round1(request):
    return render(request,'user/round1.html',{})
