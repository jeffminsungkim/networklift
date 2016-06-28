from src.resource.wordfilter import WordFilter

_author_ = 'JeffMinsungKim'

class RecentImage:


    def __init__(self, url_links, biographies, follow_list):
        self.recent_url_links = url_links
        self.biographies = biographies
        self.follow_list = follow_list
        self.length_of_recent_urls = len(self.recent_url_links)

    def fetch_approved_url_depends_on_number_of_tags(self):

        THREE_IMAGES = 3
        num_of_passed_image_link = 0
        approved_url_links = []
        temp_follow_list = []
        number_of_tags = self.length_of_recent_urls

        for tagindex in range(number_of_tags):
            if len(self.recent_url_links[tagindex]) == 0:
                self.recent_url_links.remove(self.recent_url_links[tagindex])
                number_of_tags -= 1
                break

        while any(self.recent_url_links):
            for i in range(number_of_tags):
                accord_with_tag = i * number_of_tags
                if num_of_passed_image_link == THREE_IMAGES:
                    del self.recent_url_links[:]
                    break
                else:
                    bio_is_fine = WordFilter.is_string_contains_improper_word(self.biographies[accord_with_tag])
                    for j in range(1):
                        url = self.recent_url_links[i][j]
                        if bio_is_fine and number_of_tags < 3:
                            approved_url_links.append(url)
                            self.recent_url_links[i].remove(url)
                            self.biographies.remove(self.biographies[accord_with_tag])
                            temp_follow_list.append(self.follow_list[accord_with_tag])
                            self.follow_list.remove(self.follow_list[accord_with_tag])
                            num_of_passed_image_link += 1
                        elif bio_is_fine and number_of_tags == 3:
                            approved_url_links.append(url)
                            self.recent_url_links[i].remove(url)
                            temp_follow_list.append(self.follow_list[accord_with_tag])
                            num_of_passed_image_link += 1
                        else:
                            pass

        del self.follow_list[:]
        self.follow_list = temp_follow_list

        return approved_url_links

    def fetch_approved_follow_status_depends_on_number_of_tags(self):

        number_of_follow = self.follow_list
        length_of_follows = len(number_of_follow)

        for i in range(length_of_follows):
            print(number_of_follow[i])

        return number_of_follow