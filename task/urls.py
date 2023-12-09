from django.urls import path

from .views import add_task, delete_task, edit_task, show_tasks

urlpatterns = [
    path("show-tasks/", show_tasks, name="show_tasks"),
    path("add-task/", add_task, name="add_task"),
    path("edit-task/<int:task_id>/", edit_task, name="edit_task"),
    path("delete-task/<int:task_id>/", delete_task, name="delete_task"),
]
