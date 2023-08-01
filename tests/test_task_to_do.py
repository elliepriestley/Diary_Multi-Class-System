from lib.task_to_do import TasktoDo

"""
Test that when initialising, complete property is automatically set to False
"""

def test_new_instance_tasktodo_sets_complete_property_to_false():
    task1 = TasktoDo("Walk the dog", "Tomorrow I need to walk Barney in the morning and evening")
    assert task1.complete == False

"""
Test that when using mark_complete method, complete property of the task instance is set to True
"""

def test_mark_complete_sets_complete_property_to_true():
    task1 = TasktoDo("Walk the dog", "Tomorrow I need to walk Barney in the morning and evening")
    assert task1.complete == False
    task1.mark_complete()
    assert task1.complete == True