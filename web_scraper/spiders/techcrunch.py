# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


def process_value(value):
    match = re.search(r'\d+/\d+/\d+/(.+)/', value)
    if not match:
        return None

    slug = match.group(1)
    api_pattern = 'https://techcrunch.com/wp-json/wp/v2/posts?slug={}'
    return api_pattern.format(slug)


class TechcrunchSpider(CrawlSpider):
    name = 'techcrunch'
    allowed_domains = ['techcrunch.com']
    start_urls = ['http://techcrunch.com/']

    rules = (
        Rule(
            LinkExtractor(
                allow_domains=allowed_domains,
                process_value=process_value
            ),
            callback='parse_item'
        ),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
