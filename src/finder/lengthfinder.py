
_author_ = 'JeffMinsungKim'

class LengthFinder:


    @staticmethod
    def total_length_of_list(url_list):

        length_of_urls = len(url_list)
        total_length = 0

        if length_of_urls > 1:
            for i in range(length_of_urls):
                total_length += len(url_list[i])
        else:
            return length_of_urls


        return total_length