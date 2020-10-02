from scrapy import Spider, Request
from sunglasses.items import SunglassesItem
import re

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
            title = pair.xpath('./a/span[@class="title"]/text()').extract_first()
            price = pair.xpath('./a/span[@class="price"]/text()').extract_first()
            list_price = pair.xpath('./a/span[@class="list-price"]/text()').extract_first()
            pct_off_list = pair.xpath('./a/span[@class="percentage"]/text()').extract_first()
            url = pair.xpath('./a/@href').extract_first()

            meta = {'title':title,'price':price,'list_price':list_price,'pct_off_list':pct_off_list}

            yield Request(url = url, callback = self.parse_glasses_page, meta = meta)

    def parse_glasses_page(self, response):
        attributes = response.xpath('//div[@class="attributes"]')
        features = response.xpath('//*[@id="tab-features"]/article/ul/li/text()').extract()

        item = SunglassesItem()
        item['title'] = response.meta['title']
        item['price'] = response.meta['price']
        item['list_price'] = response.meta['list_price']
        item['pct_off_list'] = response.meta['pct_off_list']
        item['condition'] = attributes.xpath('./div[@class="attribute global static condition"]/span/text()').extract_first()
        item['color'] = attributes.xpath('./div[@class="attribute global static color"]/span/text()').extract_first()
        item['size'] = attributes.xpath('./div[@class="attribute global static size"]/span/text()').extract_first()
        item['gender'] = attributes.xpath('./div[@class="attribute global static gender"]/span/text()').extract_first()
        item['sold_out'] = response.xpath('//*[@id="attribute-selector"]/div[4]/a/text()').extract_first() != 'Add to cart'
        if 'non-polarized' not in [feature.lower() for feature in features]:
            item['polarized'] = 'polarized' in [feature.lower() for feature in features]
        else:
            item['polarized'] = False
        item['url'] = response.__str__().split()[1][:-1]
        yield item


            