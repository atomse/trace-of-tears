# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TotHistoryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class TianyaPostsItem(scrapy.Item):
    title = scrapy.Field()
    posts = scrapy.Field()
    host = scrapy.Field()
