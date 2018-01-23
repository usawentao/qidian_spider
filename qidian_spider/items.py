# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QidianSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name = scrapy.Field()
    book_auth = scrapy.Field()
    book_type = scrapy.Field()
    book_status = scrapy.Field()
    book_brief = scrapy.Field()
    num_type = scrapy.Field()
    num = scrapy.Field()
