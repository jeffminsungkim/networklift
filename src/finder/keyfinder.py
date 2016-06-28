
_author_ = 'JeffMinsungKim'

class KeyFinder:

    key_begins_with_code = "code:"
    key_begins_with_caption = "caption:"
    key_begins_with_username = "username:"
    key_begins_with_count = "{count:"
    key_begins_with_biography = "biography:"
    key_begins_with_owner = "owner: {username:"
    key_ends_with_date = "date:"
    key_ends_with_likes = ", likes:"
    key_ends_with_fullname = ", full_name:"

    def __init__(self, search_front_key, search_end_key):

        self.front_key_of_the_section = search_front_key
        self.end_key_of_the_section = search_end_key