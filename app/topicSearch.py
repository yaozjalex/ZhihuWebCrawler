#coding=utf-8
import MySQLdb
from bs4 import BeautifulSoup
import time
from math import ceil
import threading
import Queue
import ConfigParser
import sys
import config

from util import get_content

class FindTopics:
    def __init__(self):
        self.db = config.init()
        self.cursor = self.db.cursor()

    def run(self):

        f = open(sys.argv[1], 'r+')
        soup = BeautifulSoup(f)

        topics = soup.findAll('div',attrs={'class':'zm-profile-section-main'})

        if topics == None:
            return

        p_str = 'INSERT IGNORE INTO TOPIC (NAME, LINK_ID, LAST_VISIT, ADD_TIME) VALUES (%s, %s, %s, %s)'

        topic_list = []
        time_now = int(time.time())

        for topic in topics:
            name = topic.get_text()
            name = name.replace(u'取消关注', '')
            name = name.replace(u'0 个回答', '')
            name = name.replace('\n', '')
            name = name.replace(u'关注', '')
            if u'个回答' in name:
                name = name[:name.index(u'个回答')-2]
            link_id = topic.find_all('a')[1].attrs[u'data-tip'][4:]
            print name
            print link_id
            topic_list = topic_list + [(name, link_id, 0, time_now)]
        self.cursor.executemany(p_str,topic_list)

        self.db.close()
        print 'All task done'


class TopicSearch(object):
    def __init__(self):
        self.topicSearch_spider = FindTopics()

if __name__ == '__main__':
    topicSearch_spider = FindTopics()
    topicSearch_spider.run()
