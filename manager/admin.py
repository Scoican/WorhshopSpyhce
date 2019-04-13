# We've said earlier that Django comes with "batteries included". You haven't
# seen anything yet. It also comes with a full-blown UI where you can create,
# update, delete and view the data that your models hold
from django.contrib import admin

from manager.constants import TaskState
from manager.models import Task, Board

# This class is the configuration that dictates how this particular models'
# data will look in the UI and how we can interact with it.
from manager.serializers import TaskSerializer


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'state', 'board']
    list_filter = ['state', 'board__user', 'board']


class BoardAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'user']
    list_filter = ['user']


# This is how we tell Django to use the class TaskAdmin as the UI configuration
# for the UI
admin.site.register(Task, TaskAdmin)
admin.site.register(Board, BoardAdmin)
