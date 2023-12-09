from django.shortcuts import redirect, render

from task.models import TaskCategory

from .forms import CategoryForm


def show_categories(request):
    tasks = TaskCategory.objects.all()
    return render(request, "show_tasks.html", {"tasks": tasks})


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_categories")
    else:
        form = CategoryForm()
    return render(request, "add_category.html", {"form": form})
