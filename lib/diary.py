from lib.diary_entry import DiaryEntry

class Diary:

    def __init__(self):
        self.entries_list = []
        self.contact_list = []

    def return_contacts(self):
        return self.contact_list

    def add(self, diary_entry):
        self.entries_list.append(diary_entry)
        if diary_entry.contact_included() == True:
            self.contact_list.append(diary_entry.contact)


    def search_by_time_and_reading_speed(self, wpm, minutes):
        if type(wpm) != int or type(minutes) != int:
            raise Exception("Invalid argument(s). Both arguments must be integers")
        
        words_user_can_read = wpm * minutes
        readable_list = []
        for entry in self.entries_list:
            if entry.count_words() > words_user_can_read:
                continue
            elif entry.count_words() <= words_user_can_read:
                readable_list.append(entry)
        if readable_list == []:
            return None
        else:
            return readable_list


    def read_all_entries(self):
        return self.entries_list