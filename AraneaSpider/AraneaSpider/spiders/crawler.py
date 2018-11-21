from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class HorseSpider(CrawlSpider): 
    name = 'Whirlaway'
    allowed_domains = ['treehouse-projects.github.io']

    start_urls = ['http://treehouse-projects.github.io/horse-land']

    rules = [Rule(LinkExtractor(allow=r'.*'), 
                    callback='parse_horses', 
                    follow=True)]

    def parse_horses(self, response): 
    # parse() method processes the information scraped from the web

        url = response.url
        title = response.css('title::text').extract()   # extracts only the title text inside html tags
        print('Page URL: {}'.format(url))
        print('Page title: {}'.format(title))
