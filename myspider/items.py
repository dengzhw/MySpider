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

class ArticlSpiderItem(scrapy.Item):
    url = scrapy.Field()    #文章链接
    icon = scrapy.Field()   #图片连接地址
    title = scrapy.Field()  #文章标题
    subtitle = scrapy.Field()   #该村副标题
    content = scrapy.Field()    #文章内容或简介
    type = scrapy.Field()       #类型
    comefrom = scrapy.Field()   #文章来自哪里
    hotmark = scrapy.Field()    #文章热门标签
    image_url = scrapy.Field()  #文章图片本地地址
