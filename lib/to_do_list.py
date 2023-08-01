class TodoList:
    # User-facing properties:
    #   to_do_list: list of instances of TaskToDo
    #   complete_list = list of complete instances of TaskToDo
    #   incomplete_list = list of incomplete instances of TaskToDo

    def __init__(self):
        # self.to_do_list: list of instances of TaskToDo
        self.to_do_list = []

    def add(self, tasktodo):
        # Parameters:
        #   tasktodo: an instance of TaskToDo
        # Side-effects:
        #   Adds the tasktodo to the self.to_do_list property of the self object
        self.to_do_list.append(tasktodo)

    def incomplete(self):
        # Parameters: None
        # Returns:
        #   a list of all TasktoDo instances marked as incomplete
        pass

    def complete(self):
        # Parameters: None
        # Returns:
        #   a list of all TasktoDo instances marked as complete
        pass
