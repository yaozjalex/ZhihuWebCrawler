from flask import Flask
import MySQLdb

app = Flask(__name__)
app.config.from_object('config')

from app import views