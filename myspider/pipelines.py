# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# coding：UTF-8

import urllib
import os
import shutil
import pymysql
import sys
reload(sys)  # reload 才能调用 setdefaultencoding 方法
sys.setdefaultencoding('utf-8')

class QuTuPipeline(object):
    def __init__(self):

        self.file = open('url_gif.txt', 'wb')

        if os.path.exists('gaoxiao'):
            shutil.rmtree("gaoxiao")
        else:
            os.mkdir("gaoxiao")

        if os.path.exists('mengchong'):
            shutil.rmtree("mengchong")
        else:
            os.mkdir("mengchong")

        if os.path.exists('retu'):
            shutil.rmtree("retu")
        else:
            os.mkdir("retu")

        if os.path.exists('ooxx'):
            shutil.rmtree("ooxx")
        else:
            os.mkdir("ooxx")
        if os.path.exists('article'):
            pass
        else:
            os.mkdir('article')


    def process_item(self, item, spider):
        if item["type"] == 'mengchong':
            if ".jpg" in item['url']:
                print ('mengchong/{0}.jpg'.format(item["title"]).strip())
                urllib.urlretrieve(item['url'], 'mengchong/{0}.jpg'.format(item['title']))
            else:
                print ('mengchong/{0}.gif'.format(item["title"]).strip())
                urllib.urlretrieve(item['url'], 'mengchong/{0}.gif'.format(item['title']))
        if item["type"] == 'meizitu':
            if ".jpg" in item['url']:
                print ('gaoxiao/{0}.jpg'.format(item["title"]).strip())
                urllib.urlretrieve(item['url'], 'gaoxiao/{0}.jpg'.format(item['title']))
            else:
                print ('gaoxiao/{0}.gif'.format(item["title"]).strip())
                urllib.urlretrieve(item['url'], 'gaoxiao/{0}.gif'.format(item['title']))

        if item["type"] == 'retu':
            if ".jpg" in item['url']:
                print ('ImageDownload retu/{0}.jpg'.format(item["title"]).strip())
                urllib.urlretrieve(item['url'], 'retu/{0}.jpg'.format(item['title']))
            else:
                print ('ImageDownload retu/{0}.gif'.format(item["title"]).strip())
                urllib.urlretrieve(item['url'], 'retu/{0}.gif'.format(item['title']))
        if item["type"] == 'ooxx':
            if ".jpg" in item['url']:
                print ('ImageDownload ooxx/{0}.jpg'.format(item["title"]).strip())
                urllib.urlretrieve(item['url'], 'ooxx/{0}.jpg'.format(item['title']))
            else:
                print ('ImageDownload ooxx/{0}.gif'.format(item["title"]).strip())
                urllib.urlretrieve(item['url'], 'ooxx/{0}.gif'.format(item['title']))

        if spider.name == "zuoan":
            if len(item['icon']):
                if ".jpg" in item['icon']:
                    print ('ImageDownload article/{0}.jpg'.format(item["title"]).strip())
                    urllib.urlretrieve(item['icon'], 'article/{0}.jpg'.format(item['title']))
                else:
                    print ('ImageDownload article/{0}.gif'.format(item["title"]).strip())
                    urllib.urlretrieve(item['icon'], 'article/{0}.gif'.format(item['title']))

        return item



    def close_spider(self, spider):
        print("Done")


class DuanZiPipeline(object):
    def __init__(self):
        self.file = open('joke.txt', 'wb')

    def process_item(self, item, spider):
        if spider.name == 'joke' or spider.name == 'xiaohua':
            self.file.write('title' + item['title'])
            self.file.write('\r\n')
            self.file.write('content' + item['content'])
            self.file.write('\r\n')

        return item

    def close_spider(self, spider):
        self.file.close()
        print("Done")



class HelloPipeline(object):
    def process_item(self, item, spider):
        dbObject = dbHandle()
        cursor = dbObject.cursor()
        sql = 'insert into joke.t_baike(userIcon,userName,content,likes,comment) values (%s,%s,%s,%s,%s)'

        try:
            cursor.execute(sql, (item['userIcon'], item['userName'], item['content'], item['like'], item['comment']))
            dbObject.commit()
        except Exception, e:
            print e
            dbObject.rollback()

        return item


def dbHandle():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='root',
        charset='utf8',
        use_unicode=False
    )
    return conn
