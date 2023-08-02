from lib.task_to_do import TasktoDo
from lib.to_do_list import TodoList
from lib.diary_entry import DiaryEntry
from lib.diary import Diary
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


"""
Test that Diary Class method add, appends the entries list property of the self object with the diaryentry instance that is passed through as an argument
"""

def test_diary_class_add_method_appends_diaryentry_instance_to_public_list():
    entry1 = DiaryEntry("title of entry", "contents of entry", {"Contact Name": "073932615"})
    diary1 = Diary()
    diary1.add(entry1)
    assert diary1.entries_list == [entry1]

"""
Test that Diary Class method add, in the case that the diary entry includes a contact number,  appends the public contact_list with the contact information.
"""

def test_Diary_Class_contact_list_method_appends_list_contact_information():
    entry1 = DiaryEntry("My Week 1", "Content of Diary Entry", {'Denise Chan': '07986527396'})
    entry2 = DiaryEntry("My Week 2", "Content of Diary Entry Two", {'Another Name': '0937263846'})
    entry3 = DiaryEntry("My Week 3", "Content of Diary Entry Three", {'Extra Name': '083629363'})
    diary2023 = Diary()
    diary2023.add(entry1)
    diary2023.add(entry2)
    diary2023.add(entry3)
    assert diary2023.contact_list == [{'Denise Chan': '07986527396'}, {'Another Name': '0937263846'}, {'Extra Name': '083629363'}]
    

"""
Test that Diary Class method contact_list returns a list of mobile numbers and their respective contact names from all instances of diary entry, when not all instances of diary entry have a contact number
"""

def test_Diary_Class_return_contacts_method_returns_list_contact_information_only_where_contact_exists():
    entry1 = DiaryEntry("My Week 1", "Content of Diary Entry", {'Denise Chan': '07986527396'})
    entry2 = DiaryEntry("My Week 2", "Content of Diary Entry Two")
    entry3 = DiaryEntry("My Week 3", "Content of Diary Entry Three", {'Extra Name': '083629363'})
    diary2023 = Diary()
    diary2023.add(entry1)
    diary2023.add(entry2)
    diary2023.add(entry3)
    assert diary2023.return_contacts() == [{'Denise Chan': '07986527396'}, {'Extra Name': '083629363'}]

"""
Test that Diary Class method contact_list returns a list of mobile numbers and their respective contact names from all instances of diary entry, when all instances of diary entry have a contact number
"""

def test_Diary_Class_return_contacts_method_returns_list_contact_information_where_all_entries_have_contact():
    entry1 = DiaryEntry("My Week 1", "Content of Diary Entry", {'Denise Chan': '07986527396'})
    entry2 = DiaryEntry("My Week 2", "Content of Diary Entry Two", {'Another Name': '0937263846'})
    entry3 = DiaryEntry("My Week 3", "Content of Diary Entry Three", {'Extra Name': '083629363'})
    diary2023 = Diary()
    diary2023.add(entry1)
    diary2023.add(entry2)
    diary2023.add(entry3)
    assert diary2023.return_contacts() == [{'Denise Chan': '07986527396'}, {'Another Name': '0937263846'}, {'Extra Name': '083629363'}]


"""
Test that Diary Class method read_all_entries returns a full list of all instances of the diaryentry class passed through the object diary instance
"""

def test_diary_class_read_all_entries_method_returns_list_of_all_diary_entries():
    entry1 = DiaryEntry("My Week 1", "Content of Diary Entry", {'Denise Chan': '07986527396'})
    entry2 = DiaryEntry("My Week 2", "Content of Diary Entry Two")
    entry3 = DiaryEntry("My Week 3", "Content of Diary Entry Three")
    diary2023 = Diary()
    diary2023.add(entry1)
    diary2023.add(entry2)
    diary2023.add(entry3)
    assert diary2023.read_all_entries() == [entry1, entry2, entry3]

"""
Test that both arguments of the Diary Class search_by_time_and_reading_speed are integers and raise an error message if they are not
"""

def test_both_arguments_for_Diary_class_search_by_time_and_reading_speed_are_integers():
    entry1 = DiaryEntry("My Week 1", "Content of Diary Entry", {'Denise Chan': '07986527396'})
    entry2 = DiaryEntry("My Week 2", "Content of Diary Entry Two")
    entry3 = DiaryEntry("My Week 3", "Content of Diary Entry Three")
    diary2023 = Diary()
    diary2023.add(entry1)
    diary2023.add(entry2)
    diary2023.add(entry3)
    with pytest.raises(Exception) as e:
        diary2023.search_by_time_and_reading_speed('3', 7)
        diary2023.search_by_time_and_reading_speed(8, '6')
        diary2023.search_by_time_and_reading_speed('3', '10')
    error_message = str(e.value)
    assert error_message == "Invalid argument(s). Both arguments must be integers"


"""Test that when Diary Class is initialised and one Diary Entry is added, the search_by_time_and_reading_speed will return None if the diary entry content is too long for the user to read, based on their time available and their reading speed """

def test_diary_class_search_by_time_and_reading_speed_method_returns_None_if_available_entry_is_too_long_to_read():
    entry1 = DiaryEntry("My Week 1", "One two three four five six seven eight nine ten", {'Denise Chan': '07986527396'})
    diary2023 = Diary()
    diary2023.add(entry1)
    assert diary2023.search_by_time_and_reading_speed(1, 1) == None

"""
Test that when Diary class ia initialised and two Diary Entries are added (one that is too long for user to read, and one that is short enough for user to read) the search_by_time_and_reading_speed will return diary entry that is not too long for the user to read, based on their time available and their reading speed
"""

def test_diary_class_search_by_time_and_reading_speed_method_returns_shorter_entry_if_other_available_entry_is_too_long_to_read():
    entry1 = DiaryEntry("My Week 1", "One two three four five six seven eight nine ten", {'Denise Chan': '07986527396'})
    entry2 = DiaryEntry("My Week 3", "One two three four")
    diary2023 = Diary()
    diary2023.add(entry1)
    diary2023.add(entry2)
    assert diary2023.search_by_time_and_reading_speed(4, 2) == [entry2]


"""
Test that when Diary class ia initialised and four Diary Entries are added (1 that is too long for user to read, and three that are short enough for user to read) the search_by_time_and_reading_speed will return the three readable diary entries in a list.
"""

def test_diary_class_search_by_time_and_reading_speed_method_returns_list_of_multiple_readable_entries():
    entry1 = DiaryEntry("My Week 1", "One two three four five six seven eight nine ten", {'Denise Chan': '07986527396'})
    entry2 = DiaryEntry("My Week 3", "One two three four")
    entry3 = DiaryEntry("My Week 3", "This is a test")
    entry4 = DiaryEntry("My Week 3", "This entry is short enough to read")
    diary2023 = Diary()
    diary2023.add(entry1)
    diary2023.add(entry2)
    diary2023.add(entry3)
    diary2023.add(entry4)
    assert diary2023.search_by_time_and_reading_speed(1, 8) == [entry2, entry3, entry4]
