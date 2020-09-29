from scrapy import Spider, Request
from sunglasses.items import SunglassesItem
import re
import math

class SunglassesSpider(Spider):
    name = 'sunglasses_spider'
    allowed_urls = ['https://www.woot.com']
    start_urls = ['https://www.woot.com/category/sport/sunglasses']

    def parse(self, response):
        text = response.xpath('//*[@id="content"]/nav[1]/div[2]/span[1]/text()').extract_first()
        num_glasses = int(re.search('\d+',re.search('of\s\d+', text).group()).group())

        url = response.xpath('//*[@id="content"]/div[1]/div[2]/ul/li[3]/a/@href').extract_first()
        url = re.sub('skip%3D24','skip%3D0', url)
        url = re.sub('top%3D24','top%3D'+str(num_glasses), url)
        url = re.sub('page_2','page_1', url)
        url = "https://www.woot.com" + url

        yield Request(url = url, callback = self.parse_glasses_list_page)

    def parse_glasses_list_page(self, response):
        glasses = response.xpath('//*[@id="content"]/div[1]/ul/li')
        for pair in glasses:
            print(pair.xpath('./a/span[@class="title"]/text()').extract_first())
            print('+'*77)
