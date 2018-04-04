import scrapy

from getdownloaddata.items import GetdownloaddataItem

class DmozSpider(scrapy.Spider):
    name = "acgrip"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "https://acg.rip/",
#        "https://acg.rip/page/2",
#        "https://acg.rip/page/3"
    ]

    def parse(self, response):
#response.selector.xpath('//span[@class="title"]/a/text()').extract()
        for sel in response.xpath('//tr'):
            item = GetdownloaddataItem()
            item['title'] = sel.xpath('td[@class="title"]/span[@class="title"]/a/text()').extract()
            item['size'] = sel.xpath('td[@class="size"]/text()').extract()
            item['link'] = sel.xpath('td[@class="action"]/a/@href').extract()
            #print(item['title'])
            yield item
