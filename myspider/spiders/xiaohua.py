import scrapy
from myspider.items import DuanZiSpiderItem


class duanziSpider(scrapy.Spider):
    name = "xiaohua"
    offset = 1
    requestUrl = "http://www.waduanzi.com/joke/page/"
    start_urls = [requestUrl + str(offset)]
    print (requestUrl)

    def parse(self, response):
        boxList = response.xpath('//div[@class="item-detail"]/h2/a/@href').extract()
        for each in boxList:
            print ("test"+each)
            yield scrapy.Request(each, callback=self.parse_item)
        self.offset += 1
        if self.offset < 20:
            yield scrapy.Request(self.requestUrl + str(self.offset), callback=self.parse)

    def parse_item(self, response):
        item = DuanZiSpiderItem()
        content = response.xpath('//div[@class="item-content"]/text()').extract()
        print (content)
        url = response.url
        title = ""
        type = 'duanzi'
        item['title'] = title
        item['subtitle'] = ''
        item['url'] = url
        item['content'] = content[0].strip()
        print (content)
        item['type'] = type
        item['image_url'] = ''
        yield item

