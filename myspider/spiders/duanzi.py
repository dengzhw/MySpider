
import scrapy
from myspider.items import DuanZiSpiderItem


class duanziSpider(scrapy.Spider):
    name = "joke"
    offset = 1
    requestUrl = "http://wengpa.com/joke/page/"
    start_urls = [requestUrl + str(offset)]
    print (requestUrl)

    def parse(self, response):
        boxList = response.xpath('//div[@class="bbbox"]')
        for each in boxList:
            item = DuanZiSpiderItem()
            url = each.xpath('./div/header/h3/a/@href').extract()
            title = each.xpath('./div/header/h3/a/text()').extract()
            content = each.xpath('./div[@class="entry-content"]/a/p/text()').extract()
            type = 'duanzi'
            item['title'] = title[0].strip()
            item['subtitle'] = ''
            item['url'] = url[0].strip()
            item['content'] = content
            print (content)
            item['type'] = type
            item['image_url'] = ''
            yield item

        self.offset += 1
        if self.offset < 1000:
            yield scrapy.Request(self.requestUrl + str(self.offset), callback=self.parse)