import os, time
from datetime import datetime

from project import app
from pymongo import MongoClient

client = MongoClient(app.config['MONGO_URI'])

db = client[app.config['MONGO_DBNAME']]
collection = db.images_collection

def save_file_in_db(filename, created_at, uid=-1, caption=''):
    collection.insert_one(
        {
            "filename": filename,
            "created_at": created_at,
            "created_by": uid,
            "caption": caption
        }
    )

def save_file(file):

    try:
        #create local images directory if not exists
        if not os.path.exists(app.config['image_upload_path']):
            os.makedirs(app.config['image_upload_path'])

        #check for valid extension
        (fname, extension)= os.path.splitext(file.filename)

        if extension not in app.config['accepted_file_types']:
            response = {"error": "Invalid extension"}
            return response

        #append ts to filename and save to directory
        created_at = int(time.time())
        final_filename = 'uploaded_images/'+fname+'_'+str(created_at)+extension
        file.save(final_filename)

        #add entry to DB
        save_file_in_db(final_filename, created_at)

    except:
        return {"error": "Error"}

    return {'message': 'Uploaded succesfully'}