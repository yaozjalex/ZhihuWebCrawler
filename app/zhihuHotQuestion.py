#coding=utf-8
from QuestionLib import QuestionLib

import MySQLdb
import time
import ConfigParser
import config

def listTopic(myQuestionLib):
  for topic in myQuestionLib.topics:
    print topic + " " + str(myQuestionLib.topics.index(topic)) + " "
  return

'''GetHotQuestionOfOneTopic'''
def hotQuestionOfTopic(myQuestionLib):
  while 1:
    print "Please enter the id of the topic you wanna search (999: return to main menu)"
    topic = raw_input()
    if topic == "999":
      return
    elif int(topic) >= len(myQuestionLib.topics):
      print "Topic not founded."
    else:
      while 1:
        print "Choose Sort Method"
        print "1. By Focus"
        print "2. By Answer"
        print "3. By Top_Answer"
        print "4. By System_recommendation"
        print "5. Return the topic selection"
        method = raw_input()
        if method == "1" or method == "2" or method == "3" or method == "4":
          printQuestions(myQuestionLib.sortQuestion(topic, method))
        elif method == "5":
          break
        else:
          print "Wrong Input!"

'''GeetHotQuestionOfAllTopic'''
def hotQuestionOfAllTopics(myQuestionLib):
  while 1:
    print "Choose Sort Method"
    print "1. By Focus"
    print "2. By Answer"
    print "3. By Top_Answer"
    print "4. By System_recommendation"
    print "5. Return to the Main Menu"
    method = raw_input()
    if method == "1" or method == "2" or method == "3" or method == "4":
      printQuestions(myQuestionLib.sortQuestion("999", method))
    elif method == "5":
      break
    else:
      print "Wrong Input!"

def printQuestions(questionList):
  for question in questionList:
    print question[1] + " Link_Id: " + str(question[2]) + " Topic: " +question[0]
    print "Focus: " + str(question[3]) + " Answer: " + str(question[4]) + " Top_Answer: " + str(question[5]) 



'''
main function
create questionLibrary of zhihuQuestion
import Data
create text-base user-interface
'''
def main():
  myQuestionLib = QuestionLib()
  db = config.init()
  cursor = db.cursor()

  '''get topic from database'''
  cursor.execute("SELECT * FROM ZHIHUHOT_FULL_DATA.QUESTION")
  results = cursor.fetchall()
  for result in results:
    if result[4] == 0 and result[5] == 0 and result[8] == 0:
      continue
    myQuestionLib.questions.append((result[1], result[2], result[3], result[4], result[5], result[8]))
    if result[1] not in myQuestionLib.topics:
      myQuestionLib.topics.append(result[1])
  while 1:
    print "Hot Quesion of Zhihu"
    print "Select Actions"
    print "1. Topics List"
    print "2. Hottest question from a topic"
    print "3. Hottest question from all topics"
    print "4. Exit"
    response = raw_input()
    if response == "1":
      listTopic(myQuestionLib)
    elif response == "2":
      hotQuestionOfTopic(myQuestionLib)
    elif response == "3":
      hotQuestionOfAllTopics(myQuestionLib)
    elif response =="4":
      db.close()
      exit()
    else:
      print "Incorrect Input, Please Enter Again"

if __name__ == '__main__':
    main()