from django.shortcuts import render, redirect
from .models import Course

def home(request):
    course = Course.objects.all()
    return render(request, 'home/course_list.html', context={'courses':course})

def detail(request,pk):
    course = Course.objects.get(id=pk)
    return render(request, 'home/course_detail.html', context={'courses':course})
