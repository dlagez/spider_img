# @Time      :2021/2/3 15:53
# @Author    :RocZhang(dlage)
import scrapy
from scrapy.loader import ItemLoader
from ..items import ImgItem


# 爬取单个页面
class img2Spider(scrapy.Spider):
    name = 'img2'
    allowed_domians = ['walltu.com']
    start_urls = [
        'https://www.walltu.com/tuku/gou/',
    ]

    def parse(self, response, **kwargs):
        # 获取单个页面的多个图片的地址
        src_list = response.xpath('//*[@id="l"]/a/img/@src').extract()
        # 遍历图片的地址， 存储在item的src变量下
        for src in src_list:
            item = ImgItem()
            item['src'] = [src]
            yield item
