# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import json

out_dir = 'tot_out'
class TotHistoryPipeline(object):
    def process_item(self, item, spider):
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        title = item['title']
        filename = '{0}/{1}.json'.format(out_dir, title)
        with open(filename, 'w') as fd:
            json.dump(dict(item), fd, ensure_ascii=False)
