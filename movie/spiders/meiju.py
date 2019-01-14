# -*- coding: utf-8 -*-
import scrapy
from movie.items import MovieItem


class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['http://www.meijutt.com/new100.html']

    def parse(self, response):
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')   # 两个class名中间两个空格
        for movie in movies:
            item = MovieItem()
            item['name'] = movie.xpath('./h5/a/text()').extract()[0]
            yield item
