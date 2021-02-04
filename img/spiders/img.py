# @Time      :2021/2/3 15:53
# @Author    :RocZhang(dlage)
import scrapy
from scrapy.loader import ItemLoader

from ..items import ImgItem


# 爬取练习
class imgSpider(scrapy.Spider):
    name = 'img'
    allowed_domians = ['walltu.com']
    start_urls = [
        'https://www.walltu.com/tuku/gou/',
    ]

    def parse(self, response, **kwargs):
        """
        @url https://www.walltu.com/tuku/gou/
        @ return items l

        """
        # 创建loader 使用response
        l = ItemLoader(item=ImgItem(), response=response)


        l.add_xpath('title', '//*[@id="nm"]/dd/b/a/text()')

        l.add_value('url', response.url)
        l.add_value('spider', self.name)
        return l.load_item()
