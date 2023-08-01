from lib.task_to_do import TasktoDo
from lib.to_do_list import TodoList

"""
Test that when we initalise the TodoList Class and take a TasktoDo instance as an argument, the add method of TodoList adds the TasktoDo instance to the public to_do_list property
"""

def test_add_method_of_todolist_appends_task_to_public_list_when_initializing():
    task1 = TasktoDo("Title", "Contents of Task")
    august_todolist = TodoList()
    august_todolist.add(task1)
    assert august_todolist.to_do_list == [task1]