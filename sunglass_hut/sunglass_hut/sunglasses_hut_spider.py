from scrapy import Spider, Request
from sunglasses.items import SunglassesItem
import re
import pandas as pd

class SunglassHutSpider(Spider):
    name = 'sunglass_hut_spider'
    allowed_urls = ['https://www.sunglasshut.com']
    start_urls = []

    urls = pd.read_csv('urls_copy.csv', header = None)
	urls.columns = ['name','url']
	
	start_urls = list(urls.url)[:5]

	def parse(self, response):
		colors_urls = response.xpath('//*[@id="colorsPdpOverlayPopup"]/div/div[3]/ul/li')
		colors_urls = colors_urls.xpath('./a/@href').extract()
		colors_urls[0] = response.__str__().split()[1]

		for color in colors_urls:
			yield Request(url = color, callback = self.parse_product_details)

	def parse_product_details(self,response):
		item = SunglassHutItem():

		item['polarized'] = bool(response.xpath('//*[@id="WC_CachedItemDisplay_div_1"]/div/div[2]/div/span/text()').extract_first())

		details = response.xpath('//*[@id="collapseOne"]/div/ul/li')
		item['name'] = details[0].xpath('.//span/text()').extract_first()
		item['upc'] = details[1].xpath('.//span/text()').extract_first()
		item['shape'] = details[2].xpath('.//span/text()').extract_first()
		item['frame_material'] = details[3].xpath('.//span/text()').extract_first()
		item['frame_color'] = details[4].xpath('.//span/text()').extract_first()
		item['lens_material'] = details[5].xpath('.//span/text()').extract_first()
		item['lens_technology'] = details[6].xpath('.//span/text()').extract_first()
		item['lens_color'] = details[7].xpath('.//span/text()').extract_first()
		item['face_shape'] = details[8].xpath('.//span/text()').extract_first()

		yield item

