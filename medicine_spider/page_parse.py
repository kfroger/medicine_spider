#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-20 下午2:04
# @Author  : mg.tone
# @Site    : 
# @File    : page_parse.py
# @company: TS Group

import os
from .pipelines import MedicineSpiderPipeline


aim_path = '/opt/data/df/text'


def main():
    for f_path, dirs, fs in os.walk(MedicineSpiderPipeline.download_path):
        for f in fs:
            source_file = os.path.join(f_path, f)
            try:
                doc = MedicineSpiderPipeline.doc_parse(source_file)
                a_file = os.path.join(aim_path, os.path.splitext(f)[0] + '.txt')
                if doc == '':
                    continue
                with open(a_file, 'w') as fw:
                    fw.write(doc)
            except Exception as e:
                print(source_file, e)


if __name__ == '__main__':
    main()
