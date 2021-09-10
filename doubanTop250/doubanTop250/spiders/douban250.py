import scrapy


class Douban250Spider(scrapy.Spider):
    name = 'douban250'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/250']

    def parse(self, response):
        response.xpath('div').getall()
