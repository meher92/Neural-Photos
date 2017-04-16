# -*- coding: utf-8 -*-
__version__ = '0.1'
from flask import Flask
import os
template_dir = os.path.abspath('view')
# static_dir = os.path.abspath('view')
app = Flask('app', template_folder=template_dir)#, static_folder='view', static_url_path='')
# app = Flask('app')
app.config['MONGO_URI'] = 'mongodb://localhost:27017/'
app.config['MONGO_DBNAME'] = 'np_db'
app.config['image_upload_path'] = 'uploaded_images'
app.config['accepted_file_types'] = ['.jpg','.jpeg']
app.config['max_file_size'] = 5*1024*1024 #=5MB (enter this value in Bytes)

from controller import *
