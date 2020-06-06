import requests
from bs4 import BeautifulSoup


class ProcessingParse(object):
    MAIN_URL: str
    HTML_PAGE: str
    exclude_urls = {'127.0.0.1', 'localhost', '0.0.0.0'}

    def __init__(self, url: str = '', *args, **kwargs):
        self.MAIN_URL = self.check_url(url)
        self.HTML_PAGE = self.get_html(self.MAIN_URL)
        self.soup = self.__init_soup(self.HTML_PAGE)

    def __init_soup(self, html: str, features='lxml') -> BeautifulSoup:
        return BeautifulSoup(html, features=features)

    def get_url(self, url) -> requests:
        try:
            return requests.get(url)
        except requests.exceptions.ConnectionError:
            return requests.get('https://google.com')
        except requests.exceptions.MissingSchema:
            return requests.get('https://google.com')

    def get_html(self, url: str) -> str:
        return self.get_url(url).text

    def is_status_200(self, url) -> bool:
        r = self.get_url(url)
        if r.status_code == 200:
            return True
        return False

    def check_url(self, url: str) -> str:
        if url != '':
            if url[-1] == '/':
                return url
            else:
                return url + '/'
        return 'https://google.com/'

    def find_page_title(self) -> str:
        try:
            return self.soup.title.text
        except AttributeError:
            return 'NoneType'

    def find_href_tag(self) -> set:
        links = {self.MAIN_URL + a['href'] if not a['href'][:4] in 'http' else a['href']
                 for a in self.soup.find_all('a', href=True)}
        return self.exclude_links(links)

    def exclude_links(self, links: set) -> set:
        links = list(links)
        from re import findall
        for i, link in enumerate(links):
            for exclude in self.exclude_urls:
                result = findall(exclude, link)
                if result:
                    links.remove(link)
        return set(links)

    def get_links_dict(self) -> dict:
        return self.links

    def get_html_text(self) -> str:
        return self.exclude_space(self.soup.text)

    def exclude_space(self, text) -> str:
        return " ".join(text.split())

    def __len__(self) -> int:
        return len(self.find_href_tag())
