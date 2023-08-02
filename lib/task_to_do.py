
class TasktoDo:
    def __init__(self, title, task):
        self.title = title
        self.task = task
        self.complete = False

    def mark_complete(self):
        self.complete = True

    def mark_incomplete(self):
        self.complete = False
