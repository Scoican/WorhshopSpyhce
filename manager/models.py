# Here is where Django defines the base class for all our models
from django.db import models
# Django comes with "batteries included". This means that it provides us
# with lot of code that can help us out-of-the-box, including a User model
# which we are going to use soon enough
from django.contrib.auth.models import User

from manager.constants import TaskState


class Board(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name


# Defining a model/database table is as simple as creating a new class
# The class attributes are the columns of the table
class Task(models.Model):
    name = models.CharField(max_length=1024)
    description = models.CharField(max_length=5000, null=True, blank=True)
    due_date = models.DateField(null=True)
    priority = models.IntegerField(default=0)
    state = models.IntegerField(choices=TaskState.CHOICES)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=False, related_name='tasks')

    def __str__(self):
        return self.name
