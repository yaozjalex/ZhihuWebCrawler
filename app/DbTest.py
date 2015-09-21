import MySQLdb
import ConfigParser
import unittest
import config
__author__ = 'Zhuojun Yao'

class DbTest(unittest.TestCase):
    '''Set up database environment for testing'''
    def setUp(self):
       self.db = config.init()
       self.cursor = self.db.cursor()

    '''Test for multiple Database Action'''
    def testInsertJoinDeleteData(self):
        '''Insert Topic '''
        p_str = 'INSERT IGNORE INTO TOPIC (NAME, LINK_ID, LAST_VISIT, ADD_TIME) VALUES (%s, %s, %s, %s)'
        param = ["Science Fiction", 1111111, 14141414, 14141414]
        self.cursor.execute(p_str, param)
        sql1 = "SELECT LINK_ID from TOPIC WHERE NAME = %s"
        sql2 = "SELECT LAST_VISIT from TOPIC WHERE NAME = %s"
        sql3 = "SELECT ADD_TIME from TOPIC WHERE NAME = %s"
        self.cursor.execute(sql1,["Science Fiction"])
        results = self.cursor.fetchall()
        self.assertTrue(results, "1111111")
        self.cursor.execute(sql2,["Science Fiction"])
        results = self.cursor.fetchall()
        self.assertTrue(results, "14141414")
        self.cursor.execute(sql3,["Science Fiction"])
        results = self.cursor.fetchall()
        self.assertTrue(results, "14141414")
        
        '''Insert Question'''
        p_str = 'INSERT IGNORE INTO QUESTION (TOPIC, NAME, LINK_ID, FOCUS, ANSWER, LAST_VISIT, ADD_TIME, TOP_ANSWER_NUMBER) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
        param = ["Science Fiction", "Hobbit", 12121212, 12, 2, 14141414, 14141414, 121]
        self.cursor.execute(p_str, param)
        sql1 = "SELECT NAME from QUESTION WHERE TOPIC = %s"
        sql2 = "SELECT LINK_ID from QUESTION WHERE TOPIC = %s"
        sql3 = "SELECT FOCUS from QUESTION WHERE TOPIC = %s"
        sql4 = "SELECT ANSWER from QUESTION WHERE TOPIC = %s"
        sql5 = "SELECT LAST_VISIT from QUESTION WHERE TOPIC = %s"
        sql6 = "SELECT ADD_TIME from QUESTION WHERE TOPIC = %s"
        sql7 = "SELECT TOP_ANSWER_NUMBER from QUESTION WHERE TOPIC = %s"
        self.cursor.execute(sql1,["Science Fiction"])
        results = self.cursor.fetchall()
        self.assertTrue(results, "Hobbit")
        self.cursor.execute(sql2,["Science Fiction"])
        results = self.cursor.fetchall()
        self.assertTrue(results, "12121212")
        self.cursor.execute(sql3,["Science Fiction"])
        results = self.cursor.fetchall()
        self.assertTrue(results, "12")
        self.cursor.execute(sql4,["Science Fiction"])
        results = self.cursor.fetchall()
        self.assertTrue(results, "2")
        self.cursor.execute(sql5,["Science Fiction"])
        results = self.cursor.fetchall()
        self.assertTrue(results, "14141414")
        self.cursor.execute(sql6,["Science Fiction"])
        results = self.cursor.fetchall()
        self.assertTrue(results, "14141414")
        self.cursor.execute(sql7,["Science Fiction"])
        results = self.cursor.fetchall()
        self.assertTrue(results, "121")

        '''Join Two Table'''
        p_str = 'SELECT TOPIC.LINK_ID, QUESTION.TOPIC, QUESTION.NAME, QUESTION.LINK_ID, QUESTION.FOCUS, QUESTION.ANSWER, QUESTION.TOP_ANSWER_NUMBER FROM TOPIC, QUESTION WHERE TOPIC.NAME = %s AND TOPIC.NAME = QUESTION.TOPIC'
        self.cursor.execute(p_str, ["Science Fiction"])
        results = self.cursor.fetchall()
        self.assertTrue(results, ("1111111", "Science Fiction", "Hobbit", "12121212", "12", "2", "121"))

        '''Delete Topic '''
        self.cursor.execute("DELETE FROM ZHIHUHOT_FULL_DATA.TOPIC WHERE NAME = %s", ["Science Fiction"])

        sql1 = "SELECT LINK_ID from TOPIC WHERE NAME = %s"
        sql2 = "SELECT LAST_VISIT from TOPIC WHERE NAME = %s"
        sql3 = "SELECT ADD_TIME from TOPIC WHERE NAME = %s"
        self.cursor.execute(sql1,["Science Fiction"])
        results = self.cursor.fetchall()
        self.assertFalse(results, "1111111")
        self.cursor.execute(sql2,["Science Fiction"])
        results = self.cursor.fetchall()
        self.assertFalse(results, "14141414")
        self.cursor.execute(sql3,["Science Fiction"])
        results = self.cursor.fetchall()
        self.assertFalse(results, "14141414")

        '''Delete Question'''
        self.cursor.execute("DELETE FROM ZHIHUHOT_FULL_DATA.QUESTION WHERE TOPIC = %s", ["Science Fiction"])
        sql1 = "SELECT NAME from QUESTION WHERE TOPIC = %s"
        sql2 = "SELECT LINK_ID from QUESTION WHERE TOPIC = %s"
        sql3 = "SELECT FOCUS from QUESTION WHERE TOPIC = %s"
        sql4 = "SELECT ANSWER from QUESTION WHERE TOPIC = %s"
        sql5 = "SELECT LAST_VISIT from QUESTION WHERE TOPIC = %s"
        sql6 = "SELECT ADD_TIME from QUESTION WHERE TOPIC = %s"
        sql7 = "SELECT TOP_ANSWER_NUMBER from QUESTION WHERE TOPIC = %s"
        self.cursor.execute(sql1,["Science Fiction"])
        results = self.cursor.fetchall()
        self.assertFalse(results, "Hobbit")
        self.cursor.execute(sql2,["Science Fiction"])
        results = self.cursor.fetchall()
        self.assertFalse(results, "12121212")
        self.cursor.execute(sql3,["Science Fiction"])
        results = self.cursor.fetchall()
        self.assertFalse(results, "12")
        self.cursor.execute(sql4,["Science Fiction"])
        results = self.cursor.fetchall()
        self.assertFalse(results, "2")
        self.cursor.execute(sql5,["Science Fiction"])
        results = self.cursor.fetchall()
        self.assertFalse(results, "14141414")
        self.cursor.execute(sql6,["Science Fiction"])
        results = self.cursor.fetchall()
        self.assertFalse(results, "14141414")
        self.cursor.execute(sql7,["Science Fiction"])
        results = self.cursor.fetchall()
        self.assertFalse(results, "121")

        self.db.close()
     
if __name__ == "__main__":
    unittest.main()