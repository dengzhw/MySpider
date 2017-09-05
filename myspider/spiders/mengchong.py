import scrapy
from myspider.items import MeiZiTuSpiderItem


class mengchongSpider(scrapy.Spider):
    name = "mengchong"
    offset = 1
    requestUrl = "http://wengpa.com/mengchong/page/"
    start_urls = [requestUrl + str(offset)]
    print (requestUrl)

    def parse(self, response):
        boxList = response.xpath('//div[@class="bbbox"]')
        for each in boxList:
            item = MeiZiTuSpiderItem()
            url = each.xpath('./div/a/img/@src').extract()
            title = each.xpath('./div[@class="new_box"]/header/h3/a/text()').extract()
            type = 'mengchong'
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
        if self.offset < 340:
            yield scrapy.Request(self.requestUrl + str(self.offset), callback=self.parse)