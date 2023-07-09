import re
import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import ALLOWED_DOMAINS, URLS


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ALLOWED_DOMAINS
    start_urls = URLS

    def parse(self, response):
        all_peps = response.css(
            'section[id=numerical-index] tbody a::attr(href)'
        )
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        pep = re.search(
            r'PEP (?P<number>\d+) – (?P<name>.*)', 
            response.css('h1.page-title::text').get()
        )
        data = {
            'number': pep.group('number'),
            'name': pep.group('name'),
            'status': response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get()
        }
        yield PepParseItem(data)
