#coding=utf-8
import MySQLdb
import ConfigParser

from util import get_content

class QuestionLib(object):
  def __init__(self):
    self.topics = []
    '''[Topic, name, linkid, focus, answer, top_answer_number] tuple'''
    self.questions = []

    '''set up database'''
    cf = ConfigParser.ConfigParser()
    cf.read("config.ini")
          
    host = cf.get("db", "host")
    port = int(cf.get("db", "port"))
    user = cf.get("db", "user")
    passwd = cf.get("db", "passwd")
    db_name = cf.get("db", "db")
    charset = cf.get("db", "charset")
    use_unicode = cf.get("db", "use_unicode")

    """connect to database"""
    self.db = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=db_name, charset=charset, use_unicode=use_unicode)
    self.cursor = self.db.cursor()

  def sortQuestion(self, topic, method):
    results = []
    if topic != "999":
      results = [t for t in self.questions if t[0] == self.topics[int(topic)]]
    else:
      results = self.questions
      '''by Focus'''
    if(method == "1"):
      return sorted(results, key=lambda x:(-x[3]))
      '''by Answer'''
    elif(method == "2"):
      return sorted(results, key=lambda x:(-x[4]))
      '''by Top Answer'''
    elif(method == "3"):
      return sorted(results, key=lambda x:(-x[5]))
    elif(method == "4"):
      return sorted(results, key=lambda x:(-x[3]/(x[4]+1)))
    else:
      return