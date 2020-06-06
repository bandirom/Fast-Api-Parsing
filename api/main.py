from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import os
from packages.parsing import ProcessingParse
from packages.db import DB


db = DB()
app = FastAPI(debug=os.environ.get('DEBUG', default=False))
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.on_event("startup")
async def startup():
    """Connect to db"""
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    """Disconnect from db"""
    await db.disconnect()


@app.get("/")
async def read_root(request: Request):
    """Render root page: '/' """
    return templates.TemplateResponse('home.html', {"request": request})


@app.get('/index')
async def index(request: Request, url: str = '', recursions: int = 0):
    """Render index page '/index'
    1. Check url empty or not
    2. Init ProcessingParse class
    3. Get title, $available_urls, context
    4. If data doesn't exist in database - create row
    5. Depends of numbers of recursions processing each url in each $available_urls
    6. Return template
    """

    if url != '':
        main_title, context, links = await get_parsed_data(url=url)

        item: dict = {'title': main_title, 'url': url, 'context': context, 'is_main': True}
        if not await db.is_exist(item):
            print('not exist - create')
            await db.save_data(item=item)
        recursive_links = await recursion_range(recursions, links)
        data = {
            'request': request,
            'recursions': recursions,
            'was_found_links': len(links),
            'main_url': item,
            'recursive_links': recursive_links,
        }
        return templates.TemplateResponse('index.html', data)
    return templates.TemplateResponse('index.html', {"request": request, 'main_url': {}})


@app.get('/search')
async def search(q: str):
    """Ajax: return 10 found scrapped records"""
    if q != '' or q != ' ':
        return await db.get_context_matched(q)


async def recursion_range(recursions: int = 0, links: set = {}) -> int:
    urls: list = []
    links = list(links)
    total_links: int = 0
    for recursion in range(recursions):
        for link in links:
            links.remove(link)
            print('links: ', len(links), 'urls:', len(urls))
            if await db.is_url_exist(link):
                continue
            title, context, url = await get_parsed_data(url=link)
            urls += url
            value: dict = {'title': title, 'url': link, 'context': context, 'is_main': False}
            await db.save_data(value)
        print('len(links): ', len(links), 'urls:', len(urls))
        total_links += len(urls)
        links += urls
        urls.clear()
    return total_links


async def get_parsed_data(url):
    soup = ProcessingParse(url=url)
    title: str = soup.find_page_title()
    context: str = soup.get_html_text()
    links: set = soup.find_href_tag()
    return title, context, links
