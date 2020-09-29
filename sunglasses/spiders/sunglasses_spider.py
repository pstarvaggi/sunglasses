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
        num_pages = math.ceil(float(num_glasses)/24)
        print('+'*77)
        print(num_pages)
        print('+'*77)

