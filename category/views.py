from django.shortcuts import get_object_or_404, redirect, render

from task.models import TaskCategory

from .forms import CategoryForm


def show_categories(request):
    categories = TaskCategory.objects.all()
    return render(request, "show_category.html", {"categories": categories})


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_categories")
    else:
        form = CategoryForm()
    return render(request, "add_category.html", {"form": form})


def edit_category(request, category_id):
    category = get_object_or_404(TaskCategory, id=category_id)

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("show_categories")
    else:
        form = CategoryForm(instance=category)

    return render(request, "edit_category.html", {"form": form, "category": category})


def delete_category(request, category_id):
    category = get_object_or_404(TaskCategory, id=category_id)

    if request.method == "POST":
        category.delete()
        return redirect("show_categories")

    return render(request, "category/delete_category.html", {"category": category})
