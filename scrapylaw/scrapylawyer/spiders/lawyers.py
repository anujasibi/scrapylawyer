# -*- coding: utf-8 -*-
import scrapy


class LawyersSpider(scrapy.Spider):
    name = 'lawyers'
    allowed_domains = ['http://www.avvo.com/all-lawyers/ny/new_york.html']
    start_urls = ['http://http://www.avvo.com/all-lawyers/ny/new_york.html/']

    def parse(self, response):
        name= response.css('.name::text').extract()
        license= response.css('.time::attr(datetime)').extract()
        avvo_rating= response.css('.smallclass::text').extract()
        user_rating= response.css('.small::text').extract()
        images= response.css('image.attr(image)').extract()
        about=response.css('card::text').extract()
        
        
    for item in zip(name,license,avvo_rating,user_rating,images,about)
         scrapped_info={
             'name':item[0],
             'license':item[1]
         }
        yield scrapped info
