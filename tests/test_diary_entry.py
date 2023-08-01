from lib.diary_entry import DiaryEntry
import pytest

"""
Test that the count words method returns an the correct integer
"""

def test_count_words_returns_correct_integer():
    entry1 = DiaryEntry("Tues 1st August", "Today I started learning about how to design a multi class program")
    assert entry1.count_words() == 12


"""
Test that the wpm argument in reading_time method is an integer, and raise Exception if it is not
"""

def test_argument_wpm_for_reading_time_method_is_int():
    entry2 = DiaryEntry("1st Aug", "This is a new diary entry")
    with pytest.raises(Exception) as e:
        entry2.reading_time("hi")
    error_message = str(e.value)
    assert error_message == "Invalid wpm: wpm argument must be an integer"


"""
Test that the reading_time method returns the correct integer
"""

def test_reading_time_method_returns_correct_integer():
    entry3 = DiaryEntry("Title", "One two three four five six seven eight nine ten")
    assert entry3.reading_time(10) == 1
    assert entry3.reading_time(5) == 2
    assert entry3.reading_time(2) == 5
    assert entry3.reading_time(1) == 10


"""
Test that it is possible to use optional argument contact to pass through a dictionary, and then this sets the public contact property to the value of the dictionary
"""

def test_diary_entry_can_take_dictionary_as_optional_argument():
    entry3 = DiaryEntry("Title", "One two three four five six seven eight nine ten", {'Marie':'0798625116'})
    assert entry3.contact == {"Marie":"0798625116"}


"""
Test if a diary entry does not have a contact number contained within it and the user tries to access it, returns empty dictionary
"""

def test_for_empty_dict_if_user_accesses_contact_where_none_exists():
    entry4 = DiaryEntry("Title", "Contents are here")
    assert entry4.contact == {}

"""
Test that contact_included returns True when there has been a contact provided
"""

def test_contact_included_returns_true_if_contact_argument_passed_through():
    entry5 = DiaryEntry("Title", "Here are some contents", {'Emily': '0798557654'})
    entry6 = DiaryEntry("Title2", "Here are some more contents", {'Sarah': '089274754'})
    entry7 = DiaryEntry("Title3", "Here are some more more contents", {'Mohsina': '9083432648'})
    assert entry5.contact_included() == True 
    assert entry6.contact_included() == True 
    assert entry7.contact_included() == True 


"""
Test contact_included returns False where there has not been a contact provided
"""

def test_contact_included_returns_false_if_contact_argument_not_passed_through():
    entry1 = DiaryEntry("Title", "Here are some contents")
    entry2 = DiaryEntry("Title", "Contents 2")
    entry3 = DiaryEntry("Title", "One two three")
    assert entry1.contact_included() == False
    assert entry2.contact_included() == False
    assert entry3.contact_included() == False