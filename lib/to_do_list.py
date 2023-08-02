from lib.task_to_do import TasktoDo

class TodoList:
    def __init__(self):
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


