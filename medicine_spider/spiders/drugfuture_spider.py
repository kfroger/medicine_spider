#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-16 下午10:19
# @Author  : mg.tone
# @Site    : 
# @File    : drugfuture_spider.py
# @Software: PyCharm

import scrapy
from medicine_spider.items import DrugFutureItem


class DrugFutureSpider(scrapy.spiders.Spider):
    name = "df"
    allowed_domains = ["drugfuture.com"]
    root_path = 'www.drugfuture.com/chp2005'
    start_urls = [
        "http://www.drugfuture.com/chp2005/query.asp?page=%d" % page for page in range(1, 67)
    ]

    def parse(self, response):
        '''
        dd
        :param response:
        :return:
        '''
        t = 2
        for sel in response.xpath('//tr/td'):
            item = DrugFutureItem()
            link = sel.xpath('./a/@href').extract()
            desc = sel.xpath('./a/text()').extract()
            # link = '%s/%s' % (DrugFutureSpider.root_path, link[0])
            if len(link) <= 0:
                t -= 1
                continue
            if t <= 0:
                break

            item['name'] = desc[0]
            item['link'] = 'http://%s/%s' % (DrugFutureSpider.root_path, link[0])

            print(item)
            yield item
