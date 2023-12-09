from django.db import models


class TaskCategory(models.Model):
    name = models.CharField(max_length=255)
