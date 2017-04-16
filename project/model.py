import os, time
from datetime import datetime

from project import app
from pymongo import MongoClient
import pymongo

client = MongoClient(app.config['MONGO_URI'])

db = client[app.config['MONGO_DBNAME']]
collection = db.images_collection

def save_file_in_db(filename, created_at, uid=-1, caption=''):
    count = collection.count()
    collection.insert_one(
        {
            "filename": filename,
            "created_at": created_at,
            "created_by": uid,
            "caption": caption,
            "file_id": count+1
        }
    )

def save_file(file_path,uid=-1):

    try:
        #create local images directory if not exists
        if not os.path.exists(app.config['image_upload_path']):
            os.makedirs(app.config['image_upload_path'])

        #check for valid extension
        (fname, extension)= os.path.splitext(file_path.filename)

        if extension not in app.config['accepted_file_types']:
            response = {"error": "Invalid extension"}
            return response

        #append ts to filename and save to directory
        created_at = int(time.time())
        final_filename = 'uploaded_images/'+fname+'_'+str(created_at)+extension
        file_path.save(final_filename)

        #add entry to DB
        save_file_in_db(final_filename, created_at, uid)

    except:
        return {"error": "Server error"}

    return {'message': 'Uploaded succesfully'}

def get_albums(last_image_index, uid=-1):
    try:
        data = list(collection.find({'created_by':uid}).sort("created_at",pymongo.DESCENDING))[last_image_index:last_image_index+10]
        albums = []
        for obj in data:
            album = {}
            album['date_str'] = datetime.fromtimestamp(obj['created_at']).strftime('%b, %d')
            album['img_url'] = obj['filename']
            album['caption'] = obj['caption']
            album['img_id'] = obj['file_id']
            albums.append(album)
    except:
        return [{"error": "Server error"}]

    return albums