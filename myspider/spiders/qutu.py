# coding = utf8

import scrapy
from myspider.items import QuTuSpiderItem


class qutuSpider(scrapy.Spider):
    name = "gaoxiao"
    offset = 1
    requestUrl = "http://wengpa.com/gaoxiao/page/"
    start_urls = [requestUrl + str(offset)]
    print (requestUrl)

    def parse(self, response):
        boxList = response.xpath('//div[@class="bbbox"]')
        for each in boxList:
            item = QuTuSpiderItem()
            url = each.xpath('./div[@class="ll_tu"]/a/img/@src').extract()
            title = each.xpath('./div[@class="new_box"]/header/h3/a/text()').extract()
            content = ''
            type = 'gaoxiao'
            item['title'] = title[0].strip()
            item['url'] = url[0].strip()
            item['content'] = content
            item['type'] = type
            item['image_url'] = '/static/qutu/gaoxiao/'
            yield item

        self.offset += 1
        if self.offset < 1000:
            yield scrapy.Request(self.requestUrl + str(self.offset), callback=self.parse)
