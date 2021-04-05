# -*- coding:utf-8 -*-
"""
@Project ：eeqa_yc 
@File    ：data_analysis.py
@IDE     ：PyCharm 
@Author  ：yc1999
@Date    ：2021/4/5 19:35 
"""
import json
import os
import logging

logging.basicConfig(
                    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
logger.addHandler(logging.FileHandler("data_analysis.py.log", 'w'))

def stat_event_category(filename):
    category_dict = dict()

    with open(filename,"r") as f:
        for example in f:
            example = json.loads(example)
            id, content, events = example['id'], example['content'], example['events']
            for event in events:
                type, mentions = event['type'], event['mentions']
                if type in category_dict:
                    category_dict[type] += 1
                else:
                    category_dict[type] = 1

    category_dict = dict( sorted(category_dict.items(), key=lambda item:item[1], reverse=True) )
    logger.info(f"{filename}: {category_dict} ")

if __name__ == '__main__':
    filenames = ['train_base.json', 'train_trans.json', 'test_base.json', 'test_trans.json']
    for filename in filenames:
        stat_event_category(filename)
