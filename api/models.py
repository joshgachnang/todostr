from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True, default=None)
    due_date = models.DateTimeField(blank=True, null=True, default=None)
    user = models.ForeignKey(User, related_name='tasks')
    archived = models.BooleanField(default=False)
    completed = models.DateTimeField(blank=True, null=True, default=None)