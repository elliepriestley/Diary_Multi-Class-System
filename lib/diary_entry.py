class DiaryEntry:

    def __init__(self, title, content, contact={}):
        self.title = title
        self.content = content
        self.contact = contact

    def count_words(self):
        word_count_contents = len(self.content.split(' '))
        return word_count_contents

    def contact_included(self):
        if self.contact != {}:
            return True
        else:
            return False