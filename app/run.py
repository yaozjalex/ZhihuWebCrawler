#coding=utf-8
import os
from topic import Topic
from question import Question

if __name__ == '__main__':
    os.system("python topicSearch.py topic.html")
    topic = Topic()
    topic.topic_spider.run()
    question = Question()
    question.question_spider.run()
