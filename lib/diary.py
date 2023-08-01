class Diary:

    def __init__(self):
        #  self.entries_list: list of instances of diary entries
        #self.contacts = dictionary of all mobile numbers, and their respective contacts from the instances of diary entries
        pass # No code here yet

    def contact_list(self):
        # Parameters: None
        # Returns:
        #   a list of mobile numbers and their respective contact names from all instances of diary entry which included a contact argument.
        pass

    def add(self, diary_entry):
        # Parameters:
        #   track: an instance of diary_entry
        # Side-effects:
        #   Adds the track to the entries_list property of the self object
        pass # No code here yet


    def search_by_time_and_reading_speed(self, wpm, minutes):
        # Parameters:
        #   wpm: integer representing the words the user can read p/minute
        #   minutes: integer representing the time the user has to read an entry
        # Side Effects:
        #   will make use of the count_words and reading_time methods of the DiaryEntry class
        # Returns:
        #   A list of the Diary entry instances that the user can read during the time they have. 
        pass # No code here yet


    def read_all_entries(self):
        # Parameters: none
        # Returns:
        #   A list of all diary_entries from the public entries_list variable.
        pass