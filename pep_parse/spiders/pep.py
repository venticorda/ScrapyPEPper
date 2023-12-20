import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):
        pages = response.css(
            'section[id=numerical-index]').css('a[href^="pep-"]')
        for page_link in pages:
            yield response.follow(page_link, callback=self.parse_pep)

    def parse_pep(self, response):
        page = response.css('section[id=pep-page-section]')
        title = response.css('h1.page-title::text').get()
        data = {
            'number': int(page.css('li::text')[2].get().replace('PEP ', '')),
            'name': title.partition('– ')[2],
            'status': response.css('dt:contains("Status") + dd ::text').get()
        }
        yield PepParseItem(data)
