# -*- coding: utf-8 -*-
import scrapy


class LawyersSpider(scrapy.Spider):
    name = 'lawyers'
    allowed_domains = ['http://www.avvo.com/all-lawyers/ny/new_york.html']
    start_urls = ['http://http://www.avvo.com/all-lawyers/ny/new_york.html/']

    def parse(self, response):
        pass
