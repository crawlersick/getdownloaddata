# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GetdownloaddataItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    title = scrapy.Field()
    string1 = scrapy.Field()
    string2 = scrapy.Field()
    string0 = scrapy.Field()
    number1 = scrapy.Field()
    number2 = scrapy.Field()
    number0 = scrapy.Field()
    link = scrapy.Field()
    size = scrapy.Field()
    getdate = scrapy.Field()
    desc = scrapy.Field()
