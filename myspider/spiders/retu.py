import scrapy
from myspider.items import DuanZiSpiderItem


class ReTuSpider(scrapy.Spider):
    name = "retu"
    offset = 1
    currentPage = 0
    requestUrl = 'http://jandan.net/pic/'
    start_urls = [requestUrl]
    print (requestUrl)

    def parse(self, response):
        boxList = response.xpath('//div[@class="text"]/p/a[@class="view_img_link"]/@href').extract()
        for each in boxList:
            print (each)
            tag = each.split('/')[-1]
            onlyIndex = tag.split('.')[0]
            subTile = response.xpath('//div[@class="author"]/strong/text()').extract()[0].strip()
            print ("test" + onlyIndex)
            print ("test" + subTile)
            print ("currentpage:   " + str(self.currentPage))
            print ("src   " + each)
            title = onlyIndex
            item = DuanZiSpiderItem()
            type = 'retu'
            lenstr = len(title)
            if lenstr >= 10:
                item['title'] = subTile + '-' + title[lenstr - 10:lenstr]
            else:
                item['title'] = subTile + '-' + title[1:lenstr]
            item['subtitle'] = ''
            item['url'] = "http:" + each
            item['content'] = ''
            item['type'] = type
            item['image_url'] = ''
            yield item
        self.offset += 1
        if self.offset < 100:
            pagestr = response.xpath('//div[@class="cp-pagenavi"]/span/text()').extract()[0][1:][:-1]
            print (pagestr)
            self.currentPage = int(pagestr)
            reStartQuestUrl = self.requestUrl + "page-" + str(self.currentPage - 1)
            print (reStartQuestUrl)
            print ("currentpage  " + str(self.currentPage - 1))
            if self.currentPage > 0:
                yield scrapy.Request(reStartQuestUrl, callback=self.parse)
