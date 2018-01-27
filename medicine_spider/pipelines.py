# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import os
import gzip
import urllib

from bs4 import BeautifulSoup
from bs4 import element


class MedicineSpiderPipeline(object):

    download_path = '/opt/data/df/htmls'

    def process_item(self, item, spider):
        '''
        处理链接
        :param item:
        :param spider:
        :return:
        '''
        file_name = os.path.join(MedicineSpiderPipeline.download_path, item['name'] + '.html')
        if not os.path.exists(file_name):
            req = urllib.request.Request(url=item['link'])
            res = urllib.request.urlopen(req)
            doc = gzip.decompress(res.read()).decode('utf-8')

            if doc != '':
                with open(file_name, 'w') as fp:
                    fp.write(doc)

    @staticmethod
    def doc_parse(cls, doc):
        '''
        网页文档处理
        :param doc:
        :return:
        '''
        hs = BeautifulSoup(open(doc), "lxml")
        context_list = list()
        for d in hs.div.children:
            if type(d) is element.NavigableString:
                continue
            for s in d.find_all('span'):
                context_list += s.string
            context_list += '\n'
        context_list.replace('：', ':')
        return context_list
