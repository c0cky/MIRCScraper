#-*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DmozItem(scrapy.Item):
    identifier = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    vid_url = scrapy.Field()

