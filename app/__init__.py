# -*- coding: utf-8 -*-
__version__ = '0.1'
from flask import Flask
import os
template_dir = os.path.abspath('view')
# static_dir = os.path.abspath('view')
app = Flask('app', template_folder=template_dir)#, static_folder='view', static_url_path='')
# app = Flask('app')
app.config['MONGO_DBNAME'] = 'testdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/testdb'
from app.controller import *