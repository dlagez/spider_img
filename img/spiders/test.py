# @Time      :2021/2/4 9:14
# @Author    :RocZhang(dlage)

import scrapy

class imgSpider(scrapy.Spider):
    name = 'test'
    allowed_domians = ['walltu.com']
    start_urls = [
        'https://www.walltu.com/tuku/gou/',
    ]
    #
    # def parse(self, response, **kwargs):
    #     # 首先使用Request访问https://www.walltu.com/tuku/gou/
    #     # Request请求完之后会带着响应response，作为callback的参数调用函数
    #     return scrapy.Request("https://www.walltu.com/tuku/gou/",
    #                           callback=self.parse_2,)
    #
    # # parse_2被callback调用，并带着返回的response
    # def parse_2(self, response):
    #     self.logger.info('Visited %s', response.url)


    def parse(self, response, **kwargs):
        request = scrapy.Request('https://www.walltu.com/tuku/gou/',
                                 callback=self.parse_2,
                                 # 这句可以看出cb_kwargs是在响应后调用的
                                 cb_kwargs=dict(main_url=response.url))
        request.cb_kwargs['foo'] = 'bar'  # 给callback增加参数
        yield request

    # parse_2被callback调用，并带着返回的response
    def parse_2(self, response, main_url, foo):
        yield dict(
            main_url=main_url,
            other_url=response.url,
            foo=foo,
        )