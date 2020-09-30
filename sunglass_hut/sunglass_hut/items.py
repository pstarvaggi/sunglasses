# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SunglassHutItem(scrapy.Item):
    brand = scrapy.Field()
    name = scrapy.Field()
    upc = scrapy.Field()
    polarized = scrapy.Field()
    shape = scrapy.Field()
    frame_color = scrapy.Field()
    frame_material = scrapy.Field()
    lens_material = scrapy.Field()
    lens_technology = scrapy.Field()
    lens_color = scrapy.Field()
    face_shape = scrapy.Field()
    price = scrapy.Field()
    list_price = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()