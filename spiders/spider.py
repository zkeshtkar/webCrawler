# -*- coding: utf-8 -*-
import scrapy

import re
from scrapy import Selector
import json

class SpiderSpider(scrapy.Spider):
    name = 'spider2'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://rahavard365.com/stock/']

    def parse(self, response):
        count = 0
        print(response)

        #Z#print("%s : %s : %s" % (response.status, response.url, response.text))
        all_rows = response.xpath('//script').extract()
        print(all_rows[10])
        #print(all_rows)

        print("finish")
