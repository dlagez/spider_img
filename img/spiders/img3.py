# @Time      :2021/2/3 15:53
# @Author    :RocZhang(dlage)


import scrapy
from scrapy.loader import ItemLoader

from ..items import ImgItem

class img2Spider(scrapy.Spider):
    name = 'img3'
    allowed_domians = ['walltu.com']
    start_urls = [
        'https://www.walltu.com/tuku/gou/',
    ]

    # 爬取多个页面
    def parse(self, response, **kwargs):
        link_list = response.xpath('//*[@id="pg"]/a/@href').extract()

        for link in link_list:
            yield scrapy.Request('http://www.walltu.com/tuku/gou/'+link, callback=self.parse_info)

    # 爬取图片
    def parse_info(self, response):
        src_list = response.xpath('//*[@id="l"]/a/img/@src').extract()
        for src in src_list:
            item = ImgItem()
            item['src'] = [src]
            yield item
