# @Time      :2021/2/4 9:33
# @Author    :RocZhang(dlage)
import scrapy
from scrapy.spidermiddlewares.httperror import HttpError


# 错误处理函数
class ErrbackSpider(scrapy.Spider):
    name = 'error'
    start_urls = [
        "https://www.walltu.com/tuku/gou/",      # 200
        "https://www.walltu.com/tuku/gou/ccc",   # 404
    ]

    # 多页面获取， 并分发
    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(u, callback=self.parse_httpbin,
                                 errback=self.errback_httpbin,
                                 dont_filter=True)

    # 处理错误链接
    def parse_httpbin(self, response):
        self.logger.info('Got successful response from ()'.format(response.url))

    def errback_httpbin(self, failure):
        # log all failures
        self.logger.error(repr(failure))

        # 查看出错信息
        if failure.check(HttpError):
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)
