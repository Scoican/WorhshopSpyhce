class TaskState:

    ACTIVE = 0
    DONE = 1
    ARCHIVED = 2

    CHOICES = [
        (ACTIVE, 'Active'),
        (DONE, 'Done'),
        (ARCHIVED, 'Archived')
    ]
