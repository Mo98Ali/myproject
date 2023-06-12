from flask import Flask
from flask_pymongo import PyMongo
import os
from datetime import datetime
import numpy as np
from pymongo import *




app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
#

app.config["MONGO_URI"] =  'mongodb://William2:AITSW23@141.37.168.25:27017/SW'
#"mongodb+srv://Williami:5VceuObgOJtWMyod@sw.1mvxof8.mongodb.net/Test?retryWrites=true&w=majority"
#setup mongodb

mongo_client = PyMongo(app)
db = mongo_client.db
username_g = "Martin"






from routes import *