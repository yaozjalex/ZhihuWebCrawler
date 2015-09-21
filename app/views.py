from flask import render_template, flash, redirect, session, url_for, request, g
from app import app
from QuestionLib import QuestionLib
import MySQLdb
import time
import ConfigParser
import config_view

questionLib = QuestionLib()
db = config_view.init()
cursor = db.cursor()

'''get topic from database'''
cursor.execute("SELECT * FROM ZHIHUHOT_FULL_DATA.QUESTION")
results = cursor.fetchall()
for result in results:
  if result[4] == 0 and result[5] == 0 and result[8] == 0:
    continue
  questionLib.questions.append((result[1], result[2], result[3], result[4], result[5], result[8]))
  if result[1] not in questionLib.topics:
    questionLib.topics.append(result[1])
  questions = questionLib.sortQuestion("999", '2')





@app.route('/')
@app.route('/index')
def index():    
    return render_template("index.html",
        title = 'Home',
        questions = questions)