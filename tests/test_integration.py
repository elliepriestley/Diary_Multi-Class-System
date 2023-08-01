from lib.task_to_do import TasktoDo
from lib.to_do_list import TodoList
import pytest

"""
Test that when we initalise the TodoList Class and take a TasktoDo instance as an argument, the add method of TodoList adds the TasktoDo instance to the public to_do_list property
"""

def test_add_method_of_todolist_appends_task_to_public_list_when_initializing():
    task1 = TasktoDo("Title", "Contents of Task")
    august_todolist = TodoList()
    august_todolist.add(task1)
    assert august_todolist.to_do_list == [task1]

"""
Test that when we initalise the TodoList Class, and we add multiple tasks, the public todolist property has all instances of tasks listed
"""

def test_add_method_of_todolist_appends_multiple_tasks_to_public_list_when_initializing():
    task1 = TasktoDo("Title", "Contents of Task")
    task2 = TasktoDo("Title2", "Contents of Task2")
    task3 = TasktoDo("Title3", "Contents of Task3")
    august_todolist = TodoList()
    august_todolist.add(task1)
    august_todolist.add(task2)
    august_todolist.add(task3)
    assert august_todolist.to_do_list == [task1, task2, task3]

""""
Test that the add method, if passing through a task where completed == True, appends the public completed_list with the task
"""

def test_that_completed_tasks_added_to_completed_list_with_add_method_of_todolist():
    task1 = TasktoDo("Title", "Contents of Task")
    task1.mark_complete()
    august_todolist = TodoList()
    august_todolist.add(task1)
    assert august_todolist.completed_list == [task1]



""""
Test that the add method in todolist class, if passing through multiple tasks, only adds the tasks that where completed == True to the public completed_list 
"""

def test_that_completed_tasks_added_to_completed_list_with_add_method_of_todolist():
    task1 = TasktoDo("Title", "Contents of Task")
    task2 = TasktoDo("Title2", "Contents of Task2")
    task3 = TasktoDo("Title3", "Contents of Task3")
    task1.mark_complete()
    task3.mark_complete()
    august_todolist = TodoList()
    august_todolist.add(task1)
    august_todolist.add(task2)
    august_todolist.add(task3)
    assert august_todolist.completed_list == [task1, task3]



"""
Test that the complete method returns a list of all completed tasks
"""

def test_complete_method_of_to_do_list_returns_list_of_all_complete_tasks():
    task1 = TasktoDo("Title", "Contents of Task")
    task2 = TasktoDo("Title2", "Contents of Task2")
    task3 = TasktoDo("Title3", "Contents of Task3")
    task1.mark_complete()
    task2.mark_complete()
    august_todolist = TodoList()
    august_todolist.add(task1)
    august_todolist.add(task2)
    august_todolist.add(task3)
    assert august_todolist.complete() == [task1, task2]


"""
Test that the incomplete method returns a list of all incompleted tasks
"""

def test_incomplete_method_of_to_do_list_returns_list_of_all_incomplete_tasks():
    task1 = TasktoDo("Title", "Contents of Task")
    task2 = TasktoDo("Title2", "Contents of Task2")
    task3 = TasktoDo("Title3", "Contents of Task3")
    task1.mark_complete()
    august_todolist = TodoList()
    august_todolist.add(task1)
    august_todolist.add(task2)
    august_todolist.add(task3)
    assert august_todolist.incomplete() == [task2, task3]


"""
Test that the update method on the ToDoList class, when passing through a task that is incomplete, with the argument True, updates the Tasktodo complete status to True
"""

def test_update_method_todolist_changes_complete_status_of_task_to_true():
    task1 = TasktoDo("Title", "Contents of Task")
    august_todolist = TodoList()
    august_todolist.add(task1)
    august_todolist.update(task1, True)
    assert task1.complete == True

"""
Test that the update method on the ToDoList class, when passing through a task that is complete, with the argument False, updates the Tasktodo complete status to False
"""

def test_update_method_todolist_changes_complete_status_of_task_to_false():
    task1 = TasktoDo("Title", "Contents of Task")
    task1.mark_complete()
    august_todolist = TodoList()
    august_todolist.add(task1)
    august_todolist.update(task1, False)
    assert task1.complete == False


"""
Test that when the update method on the ToDoList Class passes through a task that is already completed and tries to update it to complete, an Assertion error is raised
"""

def test_update_method_raises_error_when_updating_complete_task_to_complete():
    task1 = TasktoDo("Title", "Contents of Task")
    task1.mark_complete()
    august_todolist = TodoList()
    august_todolist.add(task1)
    with pytest.raises(Exception) as e:
        august_todolist.update(task1, True)
    error_message = str(e.value)
    assert error_message == "This task is already complete"



"""
Test that when the update method on the ToDoList Class passes through an incomplete task and tries to update it to incomplete, an Assertion error is raised
"""

def test_update_method_raises_error_when_updating_incomplete_task_to_incomplete():
    task1 = TasktoDo("Title", "Contents of Task")
    august_todolist = TodoList()
    august_todolist.add(task1)
    with pytest.raises(Exception) as e:
        august_todolist.update(task1, False)
    error_message = str(e.value)
    assert error_message == "This task is already incomplete"
