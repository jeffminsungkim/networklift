import random

_author_ = 'JeffMinsungKim'

class Tag:

    def __init__(self, tags):
        self.tags = tags

    def shuffle_tags(self):

        received_tags = self.tags
        length_of_tags = len(received_tags)

        if length_of_tags < 4:
            return received_tags
        else:
            random.shuffle(received_tags)

        return received_tags