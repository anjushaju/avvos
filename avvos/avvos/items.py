# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AvvosItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    licence = scrapy.Field()
    image = scrapy.Field()
    avvo_rating = scrapy.Field()
    client_rating = scrapy.Field()
    reviews = scrapy.Field()
    about_me = scrapy.Field()
    practice_areas = scrapy.Field()
    pass
