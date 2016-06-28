
_author_ = 'JeffMinsungKim'

class WordFilter:

    first_restricted_word = "push"
    second_restricted_word = "click"
    third_restricted_word = "kik"

    @staticmethod
    def is_string_contains_improper_word(string):

        if (WordFilter.first_restricted_word in string or WordFilter.second_restricted_word in string or
            WordFilter.third_restricted_word in string):
            return False
        else:
            return True

    @staticmethod
    def is_biography_null(biography):

        bio = biography
        if bio == 'null' or bio == "":
            bio = "NO BIOGRAPHY"
            bio = bio.upper()
            return bio
        else:
            bio = bio.lower()
            return bio