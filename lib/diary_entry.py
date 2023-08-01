class DiaryEntry:

    def __init__(self, title, content, *contact):
        # Parameters:
        #   title: string representing the title of the diary entry
        #   content: string representing the contents of the diary entry
        #   *contact: an optional argument that is a dictionary. Key represents the name of contact, value represents the phone number
        # Side-effects:
        #   Sets the title, content and contact properties
        self.title = title
        self.content = content
        self.contact = contact
        if contact == True:
            self.contact[contact[0]] = contact[1]
            


    def count_words(self):
        word_count_contents = len(self.content.split(' '))
        return word_count_contents

    def reading_time(self, wpm):
        if type(wpm) != int:
            raise Exception("Invalid wpm: wpm argument must be an integer")
        else:
            return self.count_words() / wpm

    def contact_included(self):
        # Parameters: None
        # Returns:
        #   boolean based on whether the instance of Diary Entry used the optional contact argument. 
        pass