import re

_author_ = 'JeffMinsungKim'

class PatternFinder:


    def __init__(self):
        self._user_code_pattern = '"code":.*?"likes":'
        self._user_name_pattern = '"owner":.*?"full_name":'
        self._user_bio_follows_pattern = '"follows":.*?"followed_by":.*?"biography":.*?"full_name":'

    def find_matchingText_by_usercode(self, response):
        response = str(response)
        pattern = re.compile(self._user_code_pattern)
        matched_text = pattern.findall(response)

        return matched_text

    def find_matchingText_by_username(self, response):
        response = str(response)
        pattern = re.compile(self._user_name_pattern)
        matched_text = pattern.findall(response)

        return matched_text

    def find_matchingText_by_bio_n_follows(self, response):
        response = str(response)
        pattern = re.compile(self._user_bio_follows_pattern)
        matched_text = pattern.findall(response)

        return matched_text