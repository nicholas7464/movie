# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 管道： 数据清洗、去重
# 持久化：写txt，csv， 写入数据库

# 是缠绕于框架将爬取spider模块和处理层pipeline分离开，是的程序更容易扩展。

class MoviePipeline(object):
    def process_item(self, item, spider):
        # 'a'追加模式， w模式会覆盖上次写的信息
        with open('my_meiju.text', 'a', encoding='utf-8') as f:
            f.write(str(item['name']) + '\n')
        return item

