#coding=utf-8
import MySQLdb
import ConfigParser
import unittest
import topicSearch 
import os
from topic import Topic
from question import Question
import config
__author__ = 'Zhuojun Yao'

class DbTest(unittest.TestCase):
    '''Set up database environment for testing'''
    def setUp(self):
        self.db = config.init()
        self.cursor = self.db.cursor()
        self.cursor.execute("DELETE FROM ZHIHUHOT_FULL_DATA.QUESTION where 1;")
        self.cursor.execute("DELETE FROM ZHIHUHOT_FULL_DATA.TOPIC where 1;")
    def testSuccessfulCrawler(self):
        '''test for getting the topics correctly'''
        os.system("python topicSearch.py test.html")

        self.cursor.execute("SELECT LINK_ID FROM ZHIHUHOT_FULL_DATA.TOPIC")
        results = [item[0] for item in  self.cursor.fetchall()]
        self.assertTrue(19551388 in results)
        self.assertTrue(len(results), 20)

        self.cursor.execute("SELECT NAME FROM ZHIHUHOT_FULL_DATA.TOPIC")
        results = [item[0] for item in  self.cursor.fetchall()]
        self.assertTrue(u'硅谷' in results)

        self.cursor.execute("SELECT * FROM ZHIHUHOT_FULL_DATA.TOPIC WHERE NAME = '硅谷'")
        results = self.cursor.fetchall()
        self.assertTrue(results[0][1], 19551388)

        '''test for getting the questions based on topics'''
        topic = Topic()
        topic.topic_spider.run()
        self.cursor.execute("SELECT FOCUS FROM ZHIHUHOT_FULL_DATA.QUESTION")
        results = [item[0] for item in self.cursor.fetchall()]
        self.assertTrue(len(results) > 0)
        for result in results:
            self.assertEqual(result, 0)

        '''test for questions information update'''
        question = Question()
        question.question_spider.run()
        self.cursor.execute("SELECT FOCUS FROM ZHIHUHOT_FULL_DATA.QUESTION ORDER BY FOCUS")
        results = [item[0] for item in self.cursor.fetchall()]
        self.assertTrue(len(results) > 0)
        temp = 0
        for result in results:
            self.assertTrue(result >= temp)
            temp = result

        '''Clean up the database after testing'''
        self.cursor.execute("DELETE FROM ZHIHUHOT_FULL_DATA.QUESTION where 1;")
        self.cursor.execute("DELETE FROM ZHIHUHOT_FULL_DATA.TOPIC where 1;")

        self.db.close()

        
if __name__ == "__main__":
    unittest.main()