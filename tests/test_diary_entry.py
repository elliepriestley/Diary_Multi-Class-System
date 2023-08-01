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
        entry3 = DiaryEntry("Title", "One two three four five six seven eight nine ten", {"Marie":"0798625116"})
        assert entry3.contact == {"Marie":"0798625116"}
