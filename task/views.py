from django.shortcuts import redirect, render

from .forms import TaskForm
from .models import TaskModel


def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, "show_tasks.html", {"tasks": tasks})


def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_tasks")
    else:
        form = TaskForm()
    return render(request, "add_task.html", {"form": form})
