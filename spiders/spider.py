# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from webCrawler.items import WebcrawlerItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://rahavard365.com/stock/']
    rules = [Rule(LinkExtractor(allow=''),callback='parse_for_url', follow=True),]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, endpoint='render.html')

    def parse(self, response):
        all_rows = response.xpath("//tbody/tr").extract()
        count = 1
        while count <= len(all_rows):
            webCrawler = WebcrawlerItem()

            webCrawler['symbol'] = response.xpath("//tbody/tr[{}]/td[1]/div/div/a[@class=\'symbol\']/text()".format(count)).extract()
            webCrawler['market'] = response.xpath("//tbody/tr[{}]/td[2]/text()".format(count)).extract()
            webCrawler['dateOfTransaction'] = response.xpath("//tbody/tr[{}]/td[3]/text()".format(count)).extract()
            webCrawler['lastPrice'] = response.xpath("//tbody/tr[{}]/td[4]/span/text()".format(count)).extract()

            webCrawler['change'] = response.xpath("//tbody/tr[{}]/td[5]/span/text()".format(count)).extract()
            webCrawler['percentChange'] = response.xpath("//tbody/tr[{}]/td[6]/span[@dir=\'ltr\']/text()".format(count)).extract()
            webCrawler['volume'] = response.xpath("//tbody/tr[{}]/td[7]/span/text()".format(count)).extract()
            webCrawler['value'] = response.xpath("//tbody/tr[{}]/td[8]/span/text()".format(count)).extract()

            webCrawler['open'] = response.xpath("//tbody/tr[{}]/td[9]/span/text()".format(count)).extract()
            webCrawler['theMost'] = response.xpath("//tbody/tr[{}]/td[10]/span/text()".format(count)).extract()
            webCrawler['theLast'] = response.xpath("//tbody/tr[{}]/td[11]/span/text()".format(count)).extract()
            webCrawler['numberOfRequests'] = response.xpath("//tbody/tr[{}]/td[12]/span/text()".format(count)).extract()

            webCrawler['demandPrice'] = response.xpath("//tbody/tr[{}]/td[13]/span/text()".format(count)).extract()
            webCrawler['supplyPrice'] = response.xpath("//tbody/tr[{}]/td[14]/span/text()".format(count)).extract()
            webCrawler['supplyCount'] = response.xpath("//tbody/tr[{}]/td[15]/span/text()".format(count)).extract()

            yield