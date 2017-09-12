# -*- coding: utf-8 -*-

import scrapy
from myspider.items import ArticlSpiderItem
import sys
reload(sys)  # reload 才能调用 setdefaultencoding 方法
sys.setdefaultencoding('utf-8')

class zuoanSpider(scrapy.Spider):
    name = "zuoan"
    offset = 1
    requestUrl = "http://www.zreading.cn/page/"
    start_urls = [requestUrl + str(offset)]
    print (requestUrl)

    def parse(self, response):
        boxList = response.xpath('//div[@class="blockGroup"]/article')
        for each in boxList:
            item = ArticlSpiderItem()
            url = each.xpath('./header/h2/a/@href').extract()
            title = each.xpath('./header/h2/a/text()').extract()
            hotmark = each.xpath('./footer/span[@itemprop="articleSection"]/a/text()').extract()
            type = 'zuoan'
            item['title'] = title[0].strip()
            item['subtitle'] = ''
            item['url'] = url[0].strip()
            item['comefrom'] = u'左岸'
            item['hotmark'] = hotmark[0].strip()
            item['type'] = type
            item['image_url'] = ''
            print ("hotmark --->"+item['hotmark'])
            data = each.extract()
            if '"block-image"' in data:
                icon = each.xpath('./div/div/@style').extract()[0].strip().split('(')[1][:-1]
                print ("icon--->"+icon)
                content = each.xpath('./div[@class="block-image"]/text()').extract()
                item['icon'] = icon
            else:
                content = each.xpath('./div[@class="block-content u-clearfix grap"]/text()').extract()
                item['icon'] = ''

            item['content'] = content
            print (content)
            yield item

        self.offset += 1
        if self.offset < 382:
            yield scrapy.Request(self.requestUrl + str(self.offset), callback=self.parse)