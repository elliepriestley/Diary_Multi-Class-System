class DiaryEntry:

    def __init__(self, title, content, contact={}):
        self.title = title
        self.content = content
        self.contact = contact


    def count_words(self):
        word_count_contents = len(self.content.split(' '))
        return word_count_contents

    def reading_time(self, wpm):
        if type(wpm) != int:
            raise Exception("Invalid wpm: wpm argument must be an integer")
        else:
            return self.count_words() / wpm

    def contact_included(self):
        if self.contact != {}:
            return True
        else:
            return False