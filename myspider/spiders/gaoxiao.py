import scrapy
from myspider.items import MeiZiTuSpiderItem


class gaoxiaoSpider(scrapy.Spider):
    name = "gaoxiaotu"
    offset = 1
    requestUrl = "http://www.waduanzi.com/lengtu/page/"
    start_urls = [requestUrl + str(offset)]
    print (requestUrl)

    def parse(self, response):
        boxList = response.xpath('//div[@class="item-detail"]')
        for each in boxList:
            item = MeiZiTuSpiderItem()
            title = each.xpath('./h2/a/text()').extract()
            type = 'meizitu'
            imgsrc = each.xpath('./div/div/a/img/@src').extract()
            imghref = each.xpath('./div/div/a/@href').extract()
            if ".jpg" in imghref:
                url = imghref
            else:
                url = imgsrc
            item['title'] = title[0].strip()
            item['subtitle'] = ''
            if len(url) >= 1:
                item['url'] = url[0].strip()
                item['content'] = ''
                item['type'] = type
                item['image_url'] = ''
                print (url)
                print (title)
                yield item

        self.offset += 1
        if self.offset < 1500:
            yield scrapy.Request(self.requestUrl + str(self.offset), callback=self.parse)
