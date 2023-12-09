from django.db import models

from category.models import TaskCategory


class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=255)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    taskAssignDate = models.DateField()
    categories = models.ManyToManyField(TaskCategory)

    def __str__(self):
        return self.task.title
