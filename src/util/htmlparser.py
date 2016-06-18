import re

from src.finder.keyfinder import KeyFinder
from src.resource.wordfilter import WordFilter

_author_ = 'JeffMinsungKim'

class HtmlParser:


    def __init__(self, matches):
        self.matches = matches
        self.URL = "https://www.instagram.com/"

    def combine_usercode_with_url(self):

        TEN_DIFFERENT_MATCHES = 10
        sizeofbundle = 0
        code_bundle = []
        list_matches = self.matches
        key_finder = KeyFinder(KeyFinder.key_begins_with_code, KeyFinder.key_ends_with_date)

        for match in range(TEN_DIFFERENT_MATCHES):
            if sizeofbundle < 3:
                try:
                    matched_text = list_matches[match]
                    matched_text = matched_text.replace('"', "")
                    code = self.extract_text_by_front_end_keywords(matched_text, key_finder)
                    caption = self.fetch_image_caption_from_text(matched_text)

                    caption_is_fine = WordFilter.is_string_contains_improper_word(caption)
                    if caption_is_fine:
                        for one in range(1,2):
                            code_bundle.append(self.URL+ "p/" + code)
                            sizeofbundle += one
                    else:
                       continue

                except Exception as e:
                    print(e)

        return code_bundle

    def fetch_image_caption_from_text(self, matched_text):

        key_finder = KeyFinder(KeyFinder.key_begins_with_caption, KeyFinder.key_ends_with_likes)
        caption = self.extract_text_by_front_end_keywords(matched_text, key_finder)

        return caption

    def combine_username_with_url(self):

        url = ""
        key_finder = KeyFinder(KeyFinder.key_begins_with_username, KeyFinder.key_ends_with_fullname)

        try:
            matched_data = self.matches
            username = matched_data[0]
            username = username.replace('"', "")
            user_name = self.extract_text_by_front_end_keywords(username, key_finder)
            url = self.URL + user_name

        except Exception as e:
            print(e)

        return url

    def fetch_user_biography_from_text(self):

        biography = ""
        key_finder = KeyFinder(KeyFinder.key_begins_with_biography, KeyFinder.key_ends_with_fullname)

        try:
            matched_data = self.matches
            matched_bio = matched_data[0]
            matched_bio = matched_bio.replace('"', "")
            biography = self.extract_text_by_front_end_keywords(matched_bio, key_finder)

        except Exception as e:
            print(e)

        return biography

    def fetch_user_follows_from_text(self):

        follows_status = []
        key_finder = KeyFinder(KeyFinder.key_begins_with_count, KeyFinder.key_ends_with_fullname)

        try:
            match = self.matches
            matched_follow = match[0]
            matched_follow = matched_follow.replace('"', "")
            follows_count = self.extract_text_by_front_end_keywords(matched_follow, key_finder)
            follows = follows_count[0]
            followed_by = follows_count[1]

            for one in range(1):
                follows_status.append(follows)
                follows_status.append(followed_by)

        except Exception as e:
            print(e)

        return follows_status

    def extract_text_by_front_end_keywords(self, matched_text, key_finder):

        matched_section = matched_text
        front_key = key_finder.front_key_of_the_section
        end_key = key_finder.end_key_of_the_section

        try:
            front_keyword = re.search(front_key, matched_section)
            end_keyword = re.search(end_key, matched_section)
            split_by_front_key = matched_section.split(front_keyword.group())
            split_by_end_key = matched_section.split(end_keyword.group())

            if front_key == key_finder.key_begins_with_code:
                item = split_by_end_key[0].replace(key_finder.key_begins_with_code, "")
                item = item.replace(",","")
                item = item.strip()
                return item
            elif front_key == key_finder.key_begins_with_caption:
                matched_section = split_by_front_key[1]
                item = matched_section.replace(end_keyword.group(), "").strip()
                item = item.lower()
                return item
            elif front_key == key_finder.key_begins_with_username:
                split_by_end_key = matched_section.split(",")
                item = split_by_end_key[0].replace(key_finder.key_begins_with_owner, "").strip()
                return item
            elif front_key == key_finder.key_begins_with_count:
                follows_list = []
                follows = split_by_front_key[1].split(",")
                follows = follows[0].replace("}", "").strip()
                followed_by = split_by_front_key[2].split(",")
                followed_by = followed_by[0].replace("}", "").strip()
                follows_list.append(follows)
                follows_list.append(followed_by)
                return follows_list
            elif front_key == key_finder.key_begins_with_biography:
                item = split_by_front_key[1].replace(end_key, "").strip()
                item = WordFilter.is_biography_null(item)
                return item
            else:
                return

        except Exception as e:
            print(e)