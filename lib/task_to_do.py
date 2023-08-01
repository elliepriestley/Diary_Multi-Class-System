

class TasktoDo:
    # User-facing properties:
    #   title: string
    #   task: string
    #   complete: boolean


    def __init__(self, title, task):
        # Parameters:
        #   title: string
        #   task: string
        # Side-effects:
        #   Sets the title and task properties, and sets the complete property to False
        self.title = title
        self.task = task
        self.complete = False

    def mark_complete(self):
        # Side Effects:
        #   Sets the instance of the task complete to True
        self.complete = True