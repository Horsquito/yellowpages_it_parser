# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YellowpagesItParserItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    website = scrapy.Field()
    phone = scrapy.Field()
    source = scrapy.Field()
    hs_code = scrapy.Field()
    product = scrapy.Field()
    date_and_time = scrapy.Field()
