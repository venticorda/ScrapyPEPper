import scrapy

from pep_parse.items import PepParseItem


PEP_URL = "peps.python.org"


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = [PEP_URL]
    start_urls = ["https://" + PEP_URL]

    def parse(self, response):
        # Ищем все ссылки на отдельные PEP'ы
        pages = response.css('a.pep.reference.internal')
        for page_link in pages:
            yield response.follow(page_link, callback=self.parse_pep)

    def parse_pep(self, response):
        page_section = response.css('section#pep-page-section')
        title = response.css('h1.page-title::text').get()
        
        # Пытаемся найти номер через заголовок
        number_text = page_section.css('h1.page-title::text').get()
        if number_text and number_text.startswith('PEP'):
            number = int(number_text.split()[1])
        else:
            # Фолбэк на li элемент (если вдруг страница другая)
            number_info = page_section.css('li:contains("PEP")::text').get()
            number = int(number_info.split()[1]) if number_info else None
        
        status = page_section.css('dt:contains("Status") + dd::text').get()

        data = {
            'number': number,
            'name': title.partition('– ')[2].strip() if '–' in title else title.strip(),
            'status': status.strip() if status else None,
        }
        yield PepParseItem(data)
