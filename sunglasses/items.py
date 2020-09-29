# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SunglassesItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    list_price = scrapy.Field()
    pct_off_list = scrapy.Field()
    stars = scrapy.Field()
    review = scrapy.Field()
    condition = scrapy.Field()
    color = scrapy.Field()
    size = scrapy.Field()
    gender = scrapy.Field()
    sold_out = scrapy.Field()
    polarized = scrapy.Field()
