
import scrapy
from myspider.items import MeiZiTuSpiderItem


class meizituSpider(scrapy.Spider):
    name = "meizitu"
    offset = 1
    requestUrl = "http://wengpa.com/meinv/page/"
    start_urls = [requestUrl + str(offset)]
    print (requestUrl)

    def parse(self, response):
        boxList = response.xpath('//div[@class="bbbox"]')
        for each in boxList:
            item = MeiZiTuSpiderItem()
            url = each.xpath('./div/a/img/@src').extract()
            title = each.xpath('./div[@class="new_box"]/header/h3/a/text()').extract()
            type = 'meizitu'
            item['title'] = title[0].strip()
            item['subtitle'] = ''
            item['url'] = url[0].strip()
            item['content'] = ''
            item['type'] = type
            item['image_url'] = ''
            print (url)
            print (title)
            yield item

        self.offset += 1
        if self.offset < 20:
            yield scrapy.Request(self.requestUrl + str(self.offset), callback=self.parse)