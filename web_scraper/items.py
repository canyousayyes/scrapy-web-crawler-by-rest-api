# -*- coding: utf-8 -*-
from scrapy import Item, Field
from scrapy.loader.processors import TakeFirst, Join, Compose


class Article(Item):
    title = Field(output_processor=TakeFirst())
    publish_date = Field(output_processor=TakeFirst())
    content = Field(
        output_processor=Compose(lambda v: filter(None, v), Join(''))
    )
    image_urls = Field()
    links = Field()
