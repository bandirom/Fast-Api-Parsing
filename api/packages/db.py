from .schemas import UrlBase
from .models import links, Links
from .database import database


class DB(object):

    def __init__(self):
        pass

    async def connect(self):
        return await database.connect()

    async def disconnect(self):
        return await database.disconnect()

    async def is_exist(self, item: UrlBase) -> bool:
        if await self.get_data(item):
            return True
        return False

    async def is_url_exist(self, url):
        return await database.fetch_one(links.select().where(Links.url == url))

    async def save_data(self, item):
        data = links.insert().values(item)
        return await database.execute(data)

    async def get_data(self, item: UrlBase):
        return await database.fetch_one(links.select().where(Links.url == item['url']))

    async def save_multiple_data(self, values):
        # query = "INSERT INTO links(title, url) VALUES (:values.title, :values.url)"
        query = links.insert().values(values)
        return await database.execute_many(query=query, values=values)

    async def save_main_url(self, item):
        url = links.insert().values(item)
        return await database.execute(url)

    async def get_main_url_list(self):
        query = f"SELECT title FROM links WHERE {Links.is_main}"
        s = await database.fetch_all(query=query)
        return [dict(result) for result in s]

    async def get_context_matched(self, sequence, size: int = 10):
        query = f"SELECT title, url FROM links  WHERE context  LIKE '% {sequence} %' limit {size};"
        return await database.fetch_all(query=query)
