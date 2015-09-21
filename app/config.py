#coding=utf-8
import MySQLdb
import ConfigParser

from util import get_content

def init():
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
  db = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=db_name, charset=charset, use_unicode=use_unicode)
  return db