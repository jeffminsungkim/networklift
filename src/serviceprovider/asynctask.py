import asyncio
import aiohttp



from src.finder.patternfinder import PatternFinder
from src.resource.recentimage import RecentImage
from src.util.htmlparser import HtmlParser

_author_ = 'JeffMinsungKim'

class AsyncTask():


    def __init__(self):
        self._url = "https://www.instagram.com/explore/tags/"


    async def fetch_user_code_url(self, url):
        async  with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response = await response.read()
                pattern_finder = PatternFinder()
                matched_text = pattern_finder.find_matchingText_by_usercode(response)
                parser = HtmlParser(matched_text)
                code_url = parser.combine_usercode_with_url()

                return code_url

    async def fetch_username_url(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response = await response.read()
                pattern_finder = PatternFinder()
                matched_text = pattern_finder.find_matchingText_by_username(response)
                parser = HtmlParser(matched_text)
                username_url = parser.combine_username_with_url()

                return username_url

    async def fetch_follows(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response = await response.read()
                pattern_finder = PatternFinder()
                matched_text = pattern_finder.find_matchingText_by_bio_n_follows(response)
                parser = HtmlParser(matched_text)
                follow_data = parser.fetch_user_follows_from_text()

                return follow_data

    async def fetch_bio(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response = await response.read()
                pattern_finder = PatternFinder()
                matched_text = pattern_finder.find_matchingText_by_bio_n_follows(response)
                parser = HtmlParser(matched_text)
                biography = parser.fetch_user_biography_from_text()

                return biography

    async def run(self, tags):

        times_requested = 0
        user_code_url = []
        user_name_url = []
        biography = []
        follow_n_follower = []

        while times_requested < 3:
            tag_length = len(tags)
            if tag_length > 0:
                for i in range(1):
                    url = self._url + tags[i]
                    code_collection_task = asyncio.ensure_future(self.fetch_user_code_url(url))
                    user_code_url.append(code_collection_task)
                    tags.remove(tags[i])
                    times_requested += 1
            else:
                break

        recent_image_link = await asyncio.gather(*user_code_url)

        for i in range(times_requested):
            link = recent_image_link[i]
            for idx in range(len(link)):
                url = link
                task = asyncio.ensure_future(self.fetch_username_url(url[idx]))
                user_name_url.append(task)

        user_url_response = await asyncio.gather(*user_name_url)

        for i in range(len(user_url_response)):
            url = user_url_response
            task = asyncio.ensure_future(self.fetch_bio(url[i]))
            biography.append(task)
            task = asyncio.ensure_future(self.fetch_follows(url[i]))
            follow_n_follower.append(task)

        bio_status = await asyncio.gather(*biography)
        follow_status = await asyncio.gather(*follow_n_follower)

        recent_image = RecentImage(recent_image_link, bio_status, follow_status)
        recent_image.fetch_approved_url_depends_on_number_of_tags()
        recent_image.fetch_approved_follow_status_depends_on_number_of_tags()