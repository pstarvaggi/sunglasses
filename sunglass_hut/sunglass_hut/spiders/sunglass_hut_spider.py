from scrapy import Spider, Request
from sunglass_hut.items import SunglassHutItem
import re
import pandas as pd

class SunglassHutSpider(Spider):
    name = 'sunglass_hut_spider'
    allowed_urls = ['https://www.sunglasshut.com']
    start_urls = []

    urls = pd.read_csv('urls_copy.csv', header = None)
    urls.columns = ['name','url']
    
    start_urls = list(urls.url)

    def parse(self, response):
        colors_urls = response.xpath('//*[@id="colorsPdpOverlayPopup"]/div/div[3]/ul/li')
        colors_urls = colors_urls.xpath('./a/@href').extract()
        colors_urls[0] = response.__str__().split()[1][:-1]

        for color in colors_urls:
            yield Request(url = color, callback = self.parse_product_details)

    def parse_product_details(self,response):
        item = SunglassHutItem()

        item['polarized'] = bool(response.xpath('//*[@id="WC_CachedItemDisplay_div_1"]/div/div[2]/div/span/text()').extract_first())

        details = response.xpath('//*[@id="collapseOne"]/div/ul/li')
        try:
            item['name'] = details[0].xpath('.//span/text()').extract_first()
        except:
            pass
        try:
            item['upc'] = details[1].xpath('.//span/text()').extract_first()
        except:
            pass
        try:
            item['shape'] = details[2].xpath('.//span/text()').extract_first()
        except:
            pass
        try:
            item['frame_material'] = details[3].xpath('.//span/text()').extract_first()
        except:
            pass
        try:
            item['frame_color'] = details[4].xpath('.//span/text()').extract_first()
        except:
            pass
        try:
            item['lens_material'] = details[5].xpath('.//span/text()').extract_first()
        except:
            pass
        try:
            item['lens_technology'] = details[6].xpath('.//span/text()').extract_first()
        except:
            pass
        try:
            item['lens_color'] = details[7].xpath('.//span/text()').extract_first()
        except:
            pass
        try:
            item['face_shape'] = details[8].xpath('.//span/text()').extract_first()
        except:
            pass

        item['brand'] = response.xpath('/html/body/nav/div/div[2]/a/text()').extract_first().strip()

        try:
            item['price'] = re.search('\d+.\d+',response.xpath('//*[@id="price"]/text()').extract_first().strip()).group()
            item['list_price'] = re.search('\d+.\d+',response.xpath('//*[@id="price"]/text()').extract_first().strip()).group()
        except:
            item['price'] = re.search('\d+.\d+',response.xpath('//*[@id="offerPrice"]/text()').extract_first().strip()).group()
            item['list_price'] = re.search('\d+.\d+',response.xpath('//*[@id="listPrice"]/text()').extract_first().strip()).group()

        item['description'] = response.xpath('//*[@id="collapseTwo"]/div/p/root/text()').extract_first()
        item['url'] = response.__str__().split()[1][:-1]
        

        yield item