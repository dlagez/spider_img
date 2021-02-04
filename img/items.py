# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class Img2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    price = Field()
    description = Field()
    address = Field()
    image_urls = Field()

    images = Field()
    locaion = Field()

    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()

class ImgItem(scrapy.Item):
    # 记录图片的src，使用管道下载
    src = scrapy.Field()