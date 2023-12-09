from django.urls import path

from .views import add_task, show_tasks

urlpatterns = [
    path("show-tasks/", show_tasks, name="show_tasks"),
    path("add-task/", add_task, name="add_task"),
]
