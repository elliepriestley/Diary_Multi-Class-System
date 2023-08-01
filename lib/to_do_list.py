from lib.task_to_do import TasktoDo

class TodoList:
    # User-facing properties:
    #   to_do_list: list of instances of TaskToDo
    #   complete_list = list of complete instances of TaskToDo
    #   incomplete_list = list of incomplete instances of TaskToDo

    def __init__(self):
        # self.to_do_list: list of instances of TaskToDo
        self.to_do_list = []
        self.completed_list = []
        self.incompleted_list = []

    def add(self, tasktodo):
        self.to_do_list.append(tasktodo)
        if tasktodo.complete == True:
            self.completed_list.append(tasktodo)
        elif tasktodo.complete == False:
            self.incompleted_list.append(tasktodo)


    def incomplete(self):
        return self.incompleted_list

    def complete(self):
        return self.completed_list
    
    def update(self, task, complete_status):
        #updates the task and changes it's complete status in the TaskToDo class
        #adds it to the correct completed/incompleted list and removes it from the corresponding opposite list.
        if complete_status == True:
            if task.complete == False:
                task.mark_complete()
            else: 
                raise Exception("This task is already complete")
        elif complete_status == False:
            if task.complete == True:
                task.mark_incomplete()
            else:
                raise Exception("This task is already incomplete")


