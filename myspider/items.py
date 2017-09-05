# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class QuTuSpiderItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    type = scrapy.Field()
    image_url = scrapy.Field()
    pass

class DuanZiSpiderItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    subtitle = scrapy.Field()
    content = scrapy.Field()
    type = scrapy.Field()
    image_url = scrapy.Field()
    pass

class MeiZiTuSpiderItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    subtitle = scrapy.Field()
    content = scrapy.Field()
    type = scrapy.Field()
    image_url = scrapy.Field()
    pass