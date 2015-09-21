#coding=utf-8
import MySQLdb
import ConfigParser
import unittest
import topicSearch 
import os
from topic import Topic
from question import Question
import config
from QuestionLib import QuestionLib
__author__ = 'Zhuojun Yao'

class SortTest(unittest.TestCase):
    '''Set up database environment for testing'''
    def setUp(self):
        self.db = config.init()
        self.cursor = self.db.cursor()
    def testSort(self):
        '''test for QuestionLibrary Methods'''
        testQ = QuestionLib()
        self.cursor.execute("SELECT * FROM ZHIHUHOT_FULL_DATA.QUESTION")
        results = self.cursor.fetchall()
        for result in results:
            if result[4] == 0 and result[5] == 0 and result[8] == 0:
                continue
            testQ.questions.append((result[1], result[2], result[3], result[4], result[5], result[8]))
            if result[1] not in testQ.topics:
                testQ.topics.append(result[1])
        print testQ.sortQuestion("1", "1")
        t = testQ.sortQuestion("1", "1")
        self.assertTrue(t[0][3] >= t[1][3])
        t = testQ.sortQuestion("1", "2")
        self.assertTrue(t[0][4] >= t[1][4])
        t = testQ.sortQuestion("1", "3")
        self.assertTrue(t[0][5] >= t[1][5])
        t = testQ.sortQuestion("1", "4")
        self.assertTrue(t[0][3]/(t[0][4]+1) >= t[1][3]/(t[1][4]+1))

        t = testQ.sortQuestion("999", "1")
        self.assertTrue(t[0][3] >= t[1][3])
        t = testQ.sortQuestion("999", "2")
        self.assertTrue(t[0][4] >= t[1][4])
        t = testQ.sortQuestion("999", "3")
        self.assertTrue(t[0][5] >= t[1][5])
        t = testQ.sortQuestion("999", "4")
        self.assertTrue(t[0][3]/(t[0][4]+1) >= t[1][3]/(t[1][4]+1))

        self.db.close()

        
if __name__ == "__main__":
    unittest.main()