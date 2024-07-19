from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages


def home_page(request):
    tasks = Task.objects.all().order_by('-id')
    return render(request, 'tasks/home_page.html', {'tasks': tasks, 'page': 'home'})


def completed_tasks(request):
    completed_tasks = Task.objects.filter(completed=True).order_by('-id')
    return render(request, 'tasks/home_page.html', {'tasks': completed_tasks, 'page': 'completed'})


def remaining_tasks(request):
    remaining_tasks = Task.objects.filter(completed=False).order_by('-id')
    return render(request, 'tasks/home_page.html', {'tasks': remaining_tasks, 'page': 'remaining'})


def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        time = request.POST.get('time')

        if title and date and time:
            task = Task(
                title=title,
                description=description,
                date=date,
                time=time
            )
            task.save()
            return redirect('home_page')
        else:
            messages.error(request, 'Please fill in all required fields.')
    else:
        return render(request, 'tasks/add_task.html')
    return render(request, 'tasks/add_task.html')


def task_detail(request, pk):
    task = get_object_or_404(Task, id=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})


def delete_confirm(request, pk):
    task = get_object_or_404(Task, id=pk)
    return render(request, 'tasks/delete_confirmation.html', {'task': task})


def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect('home_page')


def toggle_complete(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.completed = not task.completed
    task.save()
    return redirect(request.META.get("HTTP_REFERER", '/'))
