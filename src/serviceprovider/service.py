import asyncio

from src.resource.tag import Tag
from src.serviceprovider.asynctask import AsyncTask


_author_ = 'JeffMinsungKim'

class Service(AsyncTask):


    def __init__(self):
        self._tags = ["cats", "dogs", "flower", "iPhones", "pizza"]
        AsyncTask.__init__(self)

    def display_recent_link(self):

        tags = Tag(self._tags).shuffle_tags()
        print("Shuffled tags:", tags)

        loop = asyncio.get_event_loop()
        task = asyncio.ensure_future(AsyncTask.run(self, tags))
        loop.run_until_complete(task)